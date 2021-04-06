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

Tried Adobe Xd, used photoshop instead

Came up with the following 3 designs: (ballpit, ortho and whitemesh)

Liked nr. 3 the most, but not entirely satisfied.

Looked at references some more, saw the common theme of an underlying simple (usually grey or dark-blue) background. TOgether with the increase in popularity of dark-mode websites, I decided to create a darker variant of the whitemesh.

I noticed that the angle in the background were all roughly around 36deg, which is the angle of a "golden triangle". I liked this conincidence and decided to make this angle a common theme for my UI design. In pratice, the angle ended up being closer to 31deg though.

Created new design based on it. Liked it. Created designs for sub-pages. On we go.

Implemented it in html and css


# Python framework

I dont like over-engineered solutions. An SQL -database backend would be exactly that.

Instead I decided to make a semi-dynamic backend. (Only static html, but I could regenarate it by running python script anytime)

I realize there are exisitng frameworks like Jekyll (?) and whatnot, but mostly for fun I decided to build my own.

The framework would consist of template-files and configuration-files ("objects").

Template files would be similar to those used in django, and provide following tokens:

if X, ifnot X, forall and insert X

cfg-files would set variable values in either a local or global context/namespace. They could then use these values to fill templates.
Values could not just be static string, but also read from txt files or converted from markdown to html.

If you wanna see how a file like this looks like, check out the cfg-file for this very project:
(...)

Build.py would build scan the config directory for all cfg-files and execute their respective commands, thus building the website.

Additionally it would remove metadata from all pictures.
