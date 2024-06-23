Hi there! Over the years, I've had the pleasure of working on a variety of exciting projects. This page gives you a little peek into some of them and showcases my contributions and work. Keep in mind, this is just a small selection, and each project is only briefly summarized.

# Recent Projects

## CTower

Let's start with one of my more recent projects, CTower, which is currently in progress. CTower is a turn-based strategy game that I am developing with a handful of friends, with myself as the lead developer.

The game presents several technical challenges. While we are still finalizing some gameplay elements, we have established two key features: a large, dynamic map composed of hundreds of thousands of individually moving hexagons and a massive number of enemies.

Here's an early demo video I assembled:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/tMNLnyCX2Ts?si=hrgAYddpsr42-V4R" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

One of the core components of the game is the HexGrid. Despite each hexagon moving individually, the entire field operates as a single object. This is achieved by morphing the grid GPU-side through the vertex shader based on custom UV data. Each hexagon points to a specific pixel in a texture, allowing a 1024x1024 field of hexagons to be rendered efficiently. Movement, status effects, and flags are encoded as a bit-representation in a single texture, optimizing performance.
Flow-Field Pathfinding

For managing the horde of enemies (1024 in this demo), we employ a flow-field containing a direction vector for each hexagon of the HexGrid. This system enables realistic movements that account for clogging, enemy density, and dynamic obstacles. The flow-field is regularly updated using a multithreaded task with [Unity's Burst Compiler](https://docs.unity3d.com/Packages/com.unity.burst@0.2-preview.20/manual/index.html), ensuring parallel processing without impacting framerate. Enemies and their health bars are rendered using instanced rendering.

Here’s an early demo showcasing the flow-field pathfinding with a large crowd of enemies:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Hy7BPKwPA0I?si=UgGtQzsr5YaYqlys" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

Recently, we made some pivotal decisions to steer the project in a new direction. We shifted towards a turn-based combat system and significantly simplified our resource-management system.

Here's a brief demo of a more recent prototype:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/NCJms_LPzu8?si=nVZ56I-FCTU-R99V" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

Despite the considerable technical challenges, this project is very much a for-fun project with friends, hence the rather 'interesting' placeholder assets and names :D

## The Fisher's Dilemma

The Fisher's Dilemma is a foraging study I developed at the [Max-Planck Institute for Human Development](https://www.mpib-berlin.mpg.de/en). Its goal is to examine how people utilize social information to forage for resources and how their behavior shifts between cooperative and competitive environments.

The core gameplay is remarkably straightforward: Players fish from several ponds, and the analysis focuses on how long it takes them to find the optimal pond and the extent to which observing other players influences their decisions.

Here’s a demonstration video of how it looks:

[ -- COMING SOON -- ]

A major challenge in this project was the multiplayer aspect and the underlying net code. Instead of relying on existing networking libraries, I decided to push my boundaries and develop a completely new, self-made net code library specifically for this project.

This library, which I named HNetwork, functions as a client-agnostic, network-synchronized Dictionary that holds the current game state. Clients interpret and render this state for each player. Synchronization is managed through a combination of TCP and UDP packets, using self-written serializers to ensure efficient communication.

The experiment shown above represents the second iteration of this concept. The previous version was significantly simpler, featuring only two ponds and allowing players to switch ponds instantaneously.

Here’s a video of the earlier version:

[ -- COMING SOON -- ]

## WFS VR

In collaboration with [Fraunhofer IDMT](https://www.idmt.fraunhofer.de/), the Max-Planck Institute for Human Development (MPIB) has been experimenting with wave-field synthesis (WFS) setups to create immersive sound environments. Wave-field synthesis allows for the creation of sound waves from any given point of origin by superimposing a large set of individual, elementary sound waves. This occurs in real space without the need for simulated Head-Related Transfer Functions (HRTF).

My task was to explore how this technology could be combined with virtual reality (VR) to enhance ecological validity through highly immersive sound setups.

The experimental WFS setup at MPIB consisted of 64 loudspeakers and three subwoofers. This is what it looks like:

![graph](config/projects_overview/wfs_setup_img.jpg)

For the first prototype, I created a simple game where the player is placed in a large, bar-like room with telephones positioned at various locations. The objective is for the player to identify which telephone is ringing. Here’s a demonstration of this prototype:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/CWmqsejxNqI?si=P8PrBM4NTd2eG6Lf" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

The initial prototype provided valuable insights and observations, which you can read about in detail here. These findings led to the development of numerous subsequent prototypes with varying selection mechanics.

![graph](config/projects_overview/wfs_prototypes.png)

The project ultimately culminated in a version that utilizes hand-tracking for selection and features an audio guide to assist participants throughout the experiment. Take a look at the final prototype below:

[ -- COMING SOON -- ]

## Lord of the Rings Mod (Hearts of Iron IV)

The Lord of the Rings Mod for Hearts of Iron IV is probably my most prominent project. Having developed the first version back in 2018, the mod has undergone several overhauls, reboots, and iterations, improving all the way to its current state. It is still actively developed, with much-appreciated contributions from several community members, although the vast majority of the mod remains my own work.

Over the years, the mod has consistently remained one of the most popular HoI4 mods of all time, accumulating well over 100k subscribers and 9k favorites. It boasts an active and thriving Discord community of over 1k members who regularly organize multiplayer games and events.

The mod has also received substantial exposure and praise from popular content creators, whose videos have amassed hundreds of thousands of views. While there are far too many videos and reviews to list here, here are two of the most recent and popular:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/lque6c_ipzo?si=iiNJfdewvsGZnYDE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/1TIEFEgF0lU?si=ZxcTH5ljzcjmKDYG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

The mod is extensive and constitutes a full-conversion mod that entirely overhauls and reworks many of the original game's components. My work includes both gameplay elements/design and graphical work. Overhauling WWII mechanics to suit a medieval setting required substantial creativity and effort. The mod generally runs much faster and smoother than the original game, resulting in more casual, shorter games.

![image of techtree](config/projects/hoi4lotr/tech_tree.jpg)

![image of map](config/projects/hoi4lotr/designers.jpg)

The lessons I learned from working on the mod’s UI and graphical assets have been invaluable. The mod frequently receives praise for its aesthetic quality. Below are some sample screenshots showcasing just a few of its components:

![image of map](config/projects/hoi4lotr/advisors.jpg)

![image of unitmodels](config/projects/hoi4lotr/unitmodels.png)

Due to its large following and active community, several derivative works, including sub-mods, translations, and standalone spinoffs, have been launched by members of our beloved community. Here are some of the most popular ones:

![image of unitmodels](config/projects/hoi4lotr/lotr_submods.png)

Given this great interest from our community, I also developed a plethora of tools to help volunteers with the development process, including the highly useful [GFX Search tool](https://hoi4-lotrmod-team.github.io/HoI4-LotrMod/) that helps developers find GFX assets and code documentation easily.

For further information, refer to the projects [Steam Page](https://steamcommunity.com/sharedfiles/filedetails/?id=1314446921) and [github repository](https://github.com/HoI4-LOTRMod-Team/HoI4-LotrMod).

## Runners Study

The Runners Study is a VR experiment I developed at the Max-Planck Institute for Human Development (MPIB). It draws inspiration from classic street games like 'Statues' or 'Red Light, Green Light.' In this experiment, four animated monsters advance on the player at different speeds. By using eye-tracking, the participant can stop one of these monsters simply by looking at it.

The monsters have different colors and patterns, each correlating with a monster's speed. The study aims to investigate whether embedding the learning process in performing instrumental actions, where all the relationships are always visible, can aid in learning cue-outcome relationships in young children.

Building a VR study using eye-tracking, encompassing several different paradigms and variants, presented substantial technical challenges. Additionally, most of the visual design work fell on my shoulders. Given the target audience, the controls needed to be intuitive and the aesthetics child-friendly. We explored many prototypes during a lengthy development phase before finalizing the concept.

Here’s a graph-like overview of the various versions we tested:

![graph image](config/projects/monsters/monsters_graph.png)

You can view demonstration videos of nearly all these versions in [this playlist](https://www.youtube.com/watch?v=-faaWsnyqm8&list=PLh6z44emfoZ3q7JlRgubr4pCkrGtROfBY&index=2&ab_channel=BenjaminKahl), but I'll highlight the most important ones here.

One of the initial challenges was visualizing the gaze direction for the player. We experimented with using a dot, a spotlight, and a line on the ground. Many of these variations led to what I call the "floater effect" (inspired by [Floaters](https://en.wikipedia.org/wiki/Floater) that get stuck in our eyes), where the gaze is dragged in a certain direction by a small discrepancy, leading to a larger one. We found that the best solution was using a spotlight and smoothing its movements over a few frames.

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/yJ1zDCBXbtk?si=Jlh2B0Fmq-NZhC7u" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

We also tried several visual designs for the "monsters." You can see one of the early designs in the previous video, but I ultimately created a fully custom rigged and animated monster. Although I’m not a professional modeler or animator, I think it turned out quite cute.

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/EsEPrI_ubpA?si=-sI3QWj8m2QJrcs-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

Another significant challenge was designing the environments. We tested numerous concepts. While we initially liked the "circular arena" of our first versions, it seemed potentially frightening for young children to have monsters walking directly at them. Consequently, we replaced the circular track with a rectangular one and elevated the player's position to a balcony, creating a sense of distance and safety.

Here’s a demonstration video of one of our final versions:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/V05TO1v-DzA?si=e1EJ1eFq3nmKTm_h" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

# A couple of years old

## ProducerScroungers

The ProducerScroungers experiment was one of my first projects at the Max-Planck Institute for Human Development (MPIB). Built within Minecraft, this foraging game places players in a field of melons or pumpkins where they search for rewards. These rewards are either fully random or clustered together, allowing players to use social information to assess trade-offs between searching for new reward patches themselves or following other players who have found one.
Producer-Scrounger Model

The producer-scrounger model has significant precedent in psychology and has been extensively studied in animals. Here’s a classic example of this model in action by Keynan, Ridley, & Lotem (2014):

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/B1h1mDgSjOc?si=5D4QLbyWGj50YejE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

The project I developed consisted of several components. One of these was a complex Minecraft mod that handled the experiment itself: setting up fields and reward patterns, guiding players through interactive tutorials, synchronizing game states, and logging data.

After the initial pilot round, the project leader, Charley Wu, presented the preliminary results at the Cognition, Collectives, and Human Culture workshop for CogSci 2020:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/_rDE49k1ENM?si=DPf3eA84s0Fy324d" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

In addition to the Minecraft mod, this project included a substantial Python codebase for analyzing and visualizing the recorded data. This included a script that could convert any given round into a 2D bird's-eye video, showcasing each player's movements and actions:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/vUHaAhjfFVo?si=fQ-3OV75DhNu_nk0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

One of the most sophisticated components was my Unity simulation framework, which allowed us to recreate every recorded frame of a round and simulate each participant's visual field. Each object was rendered with a unique RGB value, enabling precise calculation of how much of the screen each object occupied and whether it was visible or not:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/iSZ-ewpiZWI?si=1RMLbcdRljIgzBln" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

Later, as part of my ARC-VR framework project, I recreated this entire experiment with high-fidelity graphics in Unity, enabling the experiment to be played in VR as well:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/PcTfMi3zrT4?si=PzWb75NK29Ssk7m1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

For more detailed information, please refer to our [github repository](https://github.com/charleywu/minecraftforaging), as well as our two publications, [here](https://www.biorxiv.org/content/10.1101/2021.02.03.429553v2.full.pdf) and [here](https://www.biorxiv.org/content/10.1101/2023.06.28.546887v2.full.pdf).

## CoinScrounge

CoinScrounge was a semi follow-up study to our ProducerScrounger experiment. Like its predecessor, it is a foraging game where players search for hidden reward patches on a field and observe whether other players have found something.
Technical Challenges

The most significant challenge in this project was configuring and programming the underlying netcode to ensure the multiplayer aspect worked reliably and smoothly. I used Unity Netcode for GameObjects, which was still in pre-release at that point, leading to numerous problems. After extensive troubleshooting, I managed to build a stable and reliable system, learning a lot in the process.

When I began the project, there was only an abstract concept with no defined aesthetic or "visual story" to grant it ecological validity. I eventually conceived the idea of players using metal detectors to search a field for coins, which I demonstrated with this basic, initial prototype:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/FcglXG6trLU?si=atoCPbjT4WEOYieN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

The project leadership approved this idea, leading us to the next challenge: player models. We aimed for realistic player models but ultimately decided on a gender-neutral design to avoid interfering with the experiment's results. We chose a basic humanoid mannequin:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/zVoNbsIJV84?si=-FCmNLIyL_QXBknU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Another crucial aspect was signaling to other players when someone had found a reward patch. We wanted an animation to show other players that a player was digging out coins. After testing various options, we settled on a shovel excavation animation:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/6FgAhtBAEyI?si=Qt4qd4ms516aITRp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Designing the environment was another significant task. We created many versions, each with pros and cons. Ultimately, we chose the "courtyard" version, as it was least likely to interfere with player choice, and the surrounding buildings' colors provided a simple way to highlight different experimental conditions:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/vEMAG_3U7fM?si=xMKNBLyo_oTDOpTG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

To make the experiment more interactive and engaging, we introduced a minigame where players click on appearing coins with the cursor while extracting them. To limit the effects of player skill and previous gaming experience, we significantly simplified the controls. Here is the final version:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/StMnLTMG1xk?si=qmSe4qT7Ur7zpN2W" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

The experiment also featured an extensive tutorial to introduce players to the controls and rules of the game:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/cCFCDHqYG_c?si=_4ZzkeZzMrmhWPcm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

For further information, refer to our [GitHub repository](https://github.com/DominikDeffner/VirtualCollectiveForaging) and our [publication in Nature Communications](https://rdcu.be/dCC3Z).

## Cross Street Game

Initial prototype: https://www.youtube.com/watch?v=1wq6776S-Qc&ab_channel=BenjaminKahl

Later prototype: https://www.youtube.com/watch?v=6c4KILTMhV8&ab_channel=BenjaminKahl

Due to the pandemic the project was shelved

## AutoModelCar

# Computer Graphics

## RTRad

## VXCT

# Ancient history

## SDL2Game

## FizzoFeed2

## SkincReborn

## CSGO Maps

## CS 1.6 Maps