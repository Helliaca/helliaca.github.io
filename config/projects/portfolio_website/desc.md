-- WORK IN PROGRESS --

(Intro)

Building myself a personal portfolio website has long been on my todo-list. Despite not really being a web-developer or designer, I made the decision to build the whole thing from scratch.

For starters, I would have to come up with a suitable design that would match a general theme of computer-graphics, whilst maintaining a degree of professionalism and cleanness.

Websites such as [awwwards.com](https://www.awwwards.com/) put on display some great designs to draw inspiration from. And while I did look at some samples from there, my primary ideas that I had roughly sketched out in my head were all centered around an all large background image, thus I decided to create a suitable background first, then derive the remaining design elements from that.


# The quest for a good background

My first two ideas were to either create a 'Deus Ex'-style polygonal pattern or to take the words "splash image" too literally and produce a fluid-simulation with lots of small particles.

As my primary inspiration I took a Deus Ex: MD wallpaper by [limb0ist on deviantart](https://www.deviantart.com/limb0ist/art/Deus-Ex-MD-abstract-wallpaper-525676724) as well as the splash screen image of the [Unity 2020 Editor](https://blogs.unity3d.com/es/2020/02/27/an-update-on-our-gdc-2020-plans/):

<img style="width: 50%;" alt="Deus ex style" src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e21dcca4-4037-45f3-8c4c-4b9a53dc6bc5/d8oz2r8-5111687d-05f8-4534-b838-217c00a8a0f7.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvZTIxZGNjYTQtNDAzNy00NWYzLThjNGMtNGI5YTUzZGM2YmM1XC9kOG96MnI4LTUxMTE2ODdkLTA1ZjgtNDUzNC1iODM4LTIxN2MwMGE4YTBmNy5qcGcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.gLjuvdbIYoDx7Ru64qRpped_Op-_xOcVmdIraMAMhp8">
<img style="width: 50%;" alt="Unity 2020 splash image" src="https://blogs.unity3d.com/wp-content/uploads/2020/02/Unity-GDC2020-BlogHeader-01.png">


## Methodolgy

Looking at the unity splash-screen in particular I got the idea that using a fluid simulation would be the optimal way of creating a similar arrangement of particles.

Whilst I've used Blender plenty of times in the past, I still lacked meaningful experience with its built-in *matnaflow* simulation system.

For starters I set up a basic fluid domain with a sphere as an inflow. Now it was time to create adequate geometry for the fluid to collide with in order to produce meaningful splashes for the ultimate render.

I opted to do so by employing a 2D plane-array which follows two independent Bezier-curves for each of the two spatial dimensions. This is how it ended up looking like:

![Picture of coll](config/projects/portfolio_website/Coll.jpg)

Once I let the simulation bake, I arrived at a junction with the following two options:

- I could render the fluid as a series of particles or
- as a jagged, baked triangle-mesh

This is where I split the project up into two branches. Henceforth I'll refer to the particle-render as the "*ballpit*" and to mesh-based one as the "*whitemesh*".


## The Ballpit


### First steps

The first step for the desired effect was to create a low-poly sphere that would act as the particle-object.

Additionally, I thought it would be great idea to use the particle-info node for its material and map each particle's velocity to a color-gradient. The kinetic energy of each wave or splash would thus be represented by a respective color and consequently make the final render more vivid. Later on I would also add a random factor into the mix, but this was the intermediate result:

![img of ballpit](config/projects/portfolio_website/Particle_info.jpg)

I was, however, unhappy with the overall fluid setup. Instead of a steady inflow-source I opted for upside-down, hovering cones which would, hopefully, produce more impressive splashing effects as they plummeted onto the collision-geometry. I also significantly increased the amount of particles and randomness whilst decreasing the individual particle-radius, for a tightly packed particle density. (This did force me to only render about ~15% of the particles in the preview since otherwise it would get too laggy.)

Eventually I found two different angles I was (moderately) satisfied with:

![img of ballpit](config/projects/portfolio_website/two_different_angles.jpg)


### New setup

Upon further reflection I concluded that a far superior way would be to have two waves crash into one another and to then capture the moment of their impact.
Even within the my first attempts, this approach resulted in particle-arrangements that were far closer to what I had in mind in the first place.
By decreasing gravity and setting a fairly high diffusion exponent I was ultimately able to produce the following simulation:
Have a look at this:

![img of waves](config/projects/portfolio_website/wave_crash_setup.gif)

After searching around for a bit I managed to find a nice camera angle that captured the exact moment of collision of the two waves. After increasing the number of particles further I arrived at the following render:

![img of waves](config/projects/portfolio_website/this_looks_good.jpg)

The color was quite monotonous, so I played around with the light sources as well as other parameters. After some experimenting I ended up with a similar color-scheme that the original unity plash image. I also added some depth-of-field, which ultimately led me to this constellation:

![img of waves](config/projects/portfolio_website/dof_and_more.jpg)

### Final steps

Whilst it was starting to look quite decent, the particle-clumps lacked the volumetric aspect of the original, thus I decided to include a whole separate mantaflow domain with smoke.

I used the particle-domains mesh function to bake an inflow-mesh for the smoke domain. I then shrank it (Alt+S) and applied a generous decimate modifier to only get the the thickest parts of the geometry. Naturally, since the smoke would spawn at the mesh-inflow, it would have to roughly stay in place by not being affected by gravity or other forces.

Finally, I added a plane into the background with a dark-blue base-color as well as an overlayed, randomized, purple wave-pattern. The result would be following:

![img of ballpit](config/projects/portfolio_website/first_render.png)

## The Whitemesh

### First steps

For this design I wanted a jaggy, deus-ex style triangle mesh. The parameters that seemed to produce the most suitable result would be:

- Upres: 1
- Radius: 0.05
- Smoothing-positive: 1
- Smoothing-negative: 15
- Concavity-upper: 3.5
- Concavity-lower: 1

![img of mesh](config/projects/portfolio_website/basic_mesh.jpg)

Whilst the mesh was in line with what I had in mind, the overall geometry didn't seem right, so I began experimenting. The overall fluid-simulation would have to be significantly more cohesive and way less turbulent than in the ball-pit, as a large number of floating geometry was not what I had planned.

### New frontiers

Among my ultimately discarded attempts was one where I used an almost completely still vat of fluid and applied a slight amount of stirring to it for a small amount of height-difference on the surface. I also applied an orth-camera to this particular setup, which produced the following render:

![img of mesh](config/projects/portfolio_website/orthographic_final.jpg)

I really liked the 'soapy' effect produced by a material with a high amount of subsurface-scattering, and so decided to stick with it.

Ultimately, my next major design would be a much smaller fluid-domain with an excessive amount of inflow. This would result in a rapidly filling square of high-energy particles that would produce a sort of 'valley'.

After choosing an adequate material and filling in some gaps in the geometry, I inserted some light-sources. I liked the idea of sticking to the three primary colors of the RGB-standard, which led me to this render:

![img of mesh](config/projects/portfolio_website/whitemesh_final.jpg)

# Design prototypes

## First attempts

With a suitable background chosen, the design-phase could commence properly. I tried giving 'Adobe Xd' a try since it is widely used in the web-development industry, but ended up sticking to regular old Photoshop instead.

I produced one design for each of the three background types:

<img style="width: 100%; max-width: 100%;" alt="img of designs" src="config/projects/portfolio_website/designs.jpg">

Design \#1 looked decent to me, with the blurred background on containers being a highlight. However, upon further inspection, the color scheme was way too vibrant for the intended purpose. The highly saturated mix of purple and bright-blue seemed too funky for a portfolio-website and trying to tone down the colors made the design bland.

\#2 was a significantly more minimalistic style that might be applicable to a long scrolling background. It was, however \#3 which I personally liked the most. I found that using the angular arrangement of the background picture to dictate the website's layout a neat idea and the subsurface-based background provided a distinct but not over-the-top theme. Yet I still wasn't fully satisfied, and decided to keep iterating upon it.

## Final design

After looking at some references from other developers I noticed something that most of them had in common: These websites were usually built with a mono-colored or simple gradient (usually grey or dark-blue) as the background. This provided a clean and flexible look and played into the recent popularity of 'dark-mode' websites. I decided to follow suit, and apply a darker color to design \#3 as well as simplify it a fair amount. The result was the following:

![img of design](config/projects/portfolio_website/final_design.jpg)

Although I was afraid it might be a little 'edgy', the design did ultimately satisfy me, so I proceeded to implement it in HTML and CSS. I also created designs based on it for the sub-pages of this website (projects, publications, more etc.). Now it was time to start populating it with content.


# Python framework

I'm not a big fan of over-engineered solutions, and to build an SQL database backend and serve its content dynamically would be exactly that. Instead I decided to base my website on static HTML with a semi-dynamic python backend.

There are a variety of libraries, such as Jekyll, which accomplish this goal. I decided to build my own, mostly for fun.

The framework would consist of a simple *build.py* script which, when executed, would build the website by parsing settings-objects and filling them into templates, similarly to how Django works.

## Templates

The templates work as they do in django. They are pre-built HTML files with dynamic tokens that are filled

Template files would be similar to those used in django, and provide following tokens:

- `§if X§ A §endif§`: If 'X' is defined as a variable within the current context, insert 'A' here.
- `§ifnot X§ A §endif§`: If 'X' is not defined as a variable within the current context, insert 'A' here.
- `§forall§ A §endfor§`: Insert 'A' here for all objects that are defined
- `§insert X§`: Insert the value of variable 'X' here.

Variables can be set by cfg-files and are divided into two namespaces. Globally set variables are set, as the name indicates, across all files and templates. Locally set variables are only valid for that specific file/object. Values can be set to a static string but also read from text-files or converted from markdown to html.

If you want to see how one of these cfg-files looks like, take a look at the [file for this very page](config/projects/portfolio_website/portfolio_website.cfg).

The `build.py` script scans the projects `config/` directory for cfg files and executes their respective commands in order of their priority.

Additionally, the script also checks for meta-data in image files, and offers to remove these.
