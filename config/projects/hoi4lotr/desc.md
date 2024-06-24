This <i>Hearts of Iron 4</i> mod initially started off as a small, 'play-with-friends', meme-project. After all, why would one explicitly choose *Hearts of Iron*, a world-war 2 strategy game, as the underlying fundament instead of a more fitting, medieval-based game such as *Europa Universalis*?

I believe that it was precisely this unusual clash of settings that lead to this mods unusually high popularity. At first glance, the grim, bloody and industrial reality of world war 2 seems completely unsuitable to the lovely, fantasy-setting of LotR, where near-unkillable paragons regularly fend of hordes of distinctly evil enemies.

However, upon further inspection it seems to me that LotR has at least *some* general themes that don't completely miss-align with common world-war narratives. While Tolkien seemingly denied having drawn inspiration from his experiences of both world wars, the same cannot be said for Peter Jackson and his ever-popular movie adaptations.

Within the context of this mod, merely depicting the orcs in Moria as communists or Mordor as a fascist state seems absurd, yet since it isn't completely devoid of logic or analogy, a joke is born.

### Features

After remaining in somewhat of a coma for several years, the mod has enjoyed a ressurgence starting in 2022.

One of the first things I tackled after this reboot was the tech tree. I spent a long time experimenting around in photohop, trying to come up with a suitable design and produce/find the necessary assets for it. I believe the end result looks quite good!

![image of techtree](config/projects/hoi4lotr/tech_tree.jpg)

Subsequently, I got to work on reworking our unit-models. Up until this point, our models had been reskins of the base HoI4 infantry model with rifles replaced by crossbows.

I opted to import sword+shield animations from Mixamo, and create adequate models for the mixamo rig. To complement this, I also went through the effort using custom scripts to re-map a set of spear+shield animations from the Unreal Marketplace onto this new rig.

One of the biggest challenges with models has been to maintain them reasonably low-poly. Despite the endevaour, I believe we're getting out a lot from models that are, at most 5k triangles in size.

![image of unitmodels](config/projects/hoi4lotr/unitmodels.png)

Another major step I took with the rework, was our brand-new map.

The most commonly used tool for map-generation in the HoI4 modding community is MapGen. However, MapGen always generates a brand-new map, with entirely new province-ids, state-ids etc. As such, one key challenge was to build a number of custom tools that could port all our old content (states, focus trees, units etc.) from the old map to the new one.

In addition, I took the liberty of making big changes to HoI4's default map shaders and introduce a fancy zoom-out effect that transitions the map from terrain, into a drawn paper-map.

In my opinion, custom shaders are heavily under-utilized in HoI4 modding, and I believe it helped make our mod look good as well as feel unique and immersive.

The lack of custom shaders in HoI4  modding is not without reason. I too had to overcome several hurldes and think outside the box to come up with a solution. I ended up using the alpha-channel of the cityemissive texture to store a greyscale version of the painted map. This alpha channel is usually reserved for city-lights during night, but I disabled those entirely as they didn't really fit the theme of our mod anyway.
Then, I used some arbitrary shader hokus-pokus to inject color into the drawn paper map to yield the final result.

I believe the result was worth it, as the aesthetics of our mod, and particularly our map, have been held in high praise by many players.

![image of map](config/projects/hoi4lotr/map.jpg)

Another major selling-point of our mod is it's revamped Ring-mechanic.

Believe me, this took *a lot* of scripting to get working. Using a dynamic map, a scripted GUI displays the route and location of the fellowship of the ring at any given time (including different paths), as well as the members. If the fellowship passes through a country's territory, the country can assemble a hunting party (consisting of the country's unit leaders) and attack said fellowship.

Despite being a little too RNG-based, this mechanic is a fantastic example of how procedural storytelling can take place in strategy games. It's led to some absolutely amazing (and even outright hilarious) occurences taking place. It also serves as a great foundation to include a plethora of interactions for various countries.

![image of map](config/projects/hoi4lotr/ring_mech.jpg)

Our advisor rework has likewise been very well received. As with all the UX reworks I have done, the aesthetics have been praised, and the uniqueness of some advisor traits has also found favor among many players.

![image of map](config/projects/hoi4lotr/advisors.jpg)

Speaking of aesthetics, our custom equipment designers are a more recent addition that I'm also a little too smug about ;)

![image of map](config/projects/hoi4lotr/designers.jpg)

There are many, many other aspects of the mod that I've worked on, but it's a few too many to list them all here (and always expanding), so here's an arbitrary collection of screenshots!

Our Ithilien Crisis mechanic:

![image of map](config/projects/hoi4lotr/ithilien_crisis.png)

Our custom MIOs / Guilds:

![image of map](config/projects/hoi4lotr/mios.png)

Our Elven Assembly mechanic:

![image of map](config/projects/hoi4lotr/assembly.png)

Our Galadriel's Mirror mechanic:

![image of map](config/projects/hoi4lotr/mirror.png)

Our Elven Factions mechanic:

![image of map](config/projects/hoi4lotr/loth_factions.png)

Our Gondor peasant uprising:

![image of map](config/projects/hoi4lotr/gondor_uprising.png)

Some of our custom achievements:

![image of map](config/projects/hoi4lotr/achievements.jpg)


### Coverage

The mod has remained on page 2 of the most subscribed mods of HoI4 for several years. Since the reboot, it's been on a steady trend upwards.

At the time of writing it is sitting at around 110.000 subscribers and over 8800 favourites, with a total unique subscriber count of over 250.000.

It's brought to life several sub-mods, including translations but also expansions and entire spinoff-mods. Here are some of my favourites:

![image of unitmodels](config/projects/hoi4lotr/lotr_submods.png)

It's also received significant coverage from some of HoI4's most well-known content creators, including (but not limited to):

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/lque6c_ipzo?si=iiNJfdewvsGZnYDE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/1TIEFEgF0lU?si=ZxcTH5ljzcjmKDYG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

The mod's development remains active and maintains a thriving discord community that organizes regular multiplayer games. I am very excited to continue seeing this project grow!