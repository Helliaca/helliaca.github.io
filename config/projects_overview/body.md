Hi there! Over the years, I've had the pleasure of working on a variety of exciting projects. This page gives you a little peek into some of them and showcases my contributions and work. Keep in mind, this is just a small selection, and each project is only briefly summarized.

## Lord of the Rings Mod (Hearts of Iron IV)

<div class="overview-toolbar-links">
	<a aria-label="Link to pdf" href="build/projects/hoi4lotr/detailed.html" class="no-fade"><i class="fas fa-external-link-alt"></i> <b>Project Page</b></a>
	<a aria-label="Link to pdf" href="https://steamcommunity.com/sharedfiles/filedetails/?id=1314446921" class="no-fade"><i class="fab fa-steam"></i> <b>Steam Page</b></a>
	<a aria-label="Link to pdf" href="https://github.com/Helliaca/HoI4-LotrMod" class="no-fade"><i class="fab fa-github"></i> <b>Github Page</b></a>
</div>

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


## CTower

<div class="overview-toolbar-links">
	<a aria-label="Link to pdf" href="build/projects/ctower/detailed.html" class="no-fade"><i class="fas fa-external-link-alt"></i> <b>Project Page</b></a>
</div>

Let's proceed with one of my more recent projects, CTower, which is currently still in progress. CTower is a turn-based strategy game that I am developing with a handful of friends, with myself as the lead developer.

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

## Fisherman's Dilemma

<div class="overview-toolbar-links">
	<a aria-label="Link to pdf" href="build/projects/fishing_dilemma/detailed.html" class="no-fade"><i class="fas fa-external-link-alt"></i> <b>Project Page</b></a>
</div>

The Fisher's Dilemma is a foraging study I developed at the [Max-Planck Institute for Human Development](https://www.mpib-berlin.mpg.de/en). Its goal is to examine how people utilize social information to forage for resources and how their behavior shifts between cooperative and competitive environments.

The core gameplay is remarkably straightforward: Players fish from several ponds, and the analysis focuses on how long it takes them to find the optimal pond and the extent to which observing other players influences their decisions.

Here’s a demonstration video of how it looks:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/vxSoKIp9HFo?si=YIclpJscaybUWhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

A major challenge in this project was the multiplayer aspect and the underlying net code. Instead of relying on existing networking libraries, I decided to push my boundaries and develop a completely new, self-made net code library specifically for this project.

This library, which I named HNetwork, functions as a client-agnostic, network-synchronized Dictionary that holds the current game state. Clients interpret and render this state for each player. Synchronization is managed through a combination of TCP and UDP packets, using self-written serializers to ensure efficient communication.

## WFS VR

<div class="overview-toolbar-links">
	<a aria-label="Link to pdf" href="build/projects/wfs_vr/detailed.html" class="no-fade"><i class="fas fa-external-link-alt"></i> <b>Project Page</b></a>
</div>

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

## Runners Study

<div class="overview-toolbar-links">
	<a aria-label="Link to pdf" href="build/projects/monsters/detailed.html" class="no-fade"><i class="fas fa-external-link-alt"></i> <b>Project Page</b></a>
</div>

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

## ProducerScroungers

<div class="overview-toolbar-links">
	<a aria-label="Link to pdf" href="build/projects/producerscrounger/detailed.html" class="no-fade"><i class="fas fa-external-link-alt"></i> <b>Project Page</b></a>
	<a aria-label="Link to pdf" href="https://www.biorxiv.org/content/10.1101/2021.02.03.429553v2.full.pdf" class="no-fade"><i class="far fa-file-pdf"></i> <b>Publication</b></a>
	<a aria-label="Link to pdf" href="https://github.com/charleywu/minecraftforaging" class="no-fade"><i class="fab fa-github"></i> <b>Github Page</b></a>
</div>

The ProducerScroungers experiment was one of my first projects at the Max-Planck Institute for Human Development (MPIB). Built within Minecraft, this foraging game places players in a field of melons or pumpkins where they search for rewards. These rewards are either fully random or clustered together, allowing players to use social information to assess trade-offs between searching for new reward patches themselves or following other players who have found one.

The project I developed consisted of several components. One of these was a complex Minecraft mod that handled the experiment itself: setting up fields and reward patterns, guiding players through interactive tutorials, synchronizing game states, and logging data.

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

<div class="overview-toolbar-links">
	<a aria-label="Link to pdf" href="build/projects/coinscrounge/detailed.html" class="no-fade"><i class="fas fa-external-link-alt"></i> <b>Project Page</b></a>
	<a aria-label="Link to pdf" href="https://rdcu.be/dCC3Z" class="no-fade"><i class="far fa-file-pdf"></i> <b>Publication</b></a>
	<a aria-label="Link to pdf" href="https://github.com/DominikDeffner/VirtualCollectiveForaging" class="no-fade"><i class="fab fa-github"></i> <b>Github Page</b></a>
</div>

CoinScrounge was a semi follow-up study to our ProducerScrounger experiment. Like its predecessor, it is a foraging game where players search for hidden reward patches on a field and observe whether other players have found something.
Technical Challenges

The most significant challenge in this project was configuring and programming the underlying netcode to ensure the multiplayer aspect worked reliably and smoothly. I used Unity Netcode for GameObjects, which was still in pre-release at that point, leading to numerous problems. After extensive troubleshooting, I managed to build a stable and reliable system, learning a lot in the process.

When I began the project, there was only an abstract concept with no defined aesthetic or "visual story" to grant it ecological validity. I eventually conceived the idea of players using metal detectors to search a field for coins.

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/StMnLTMG1xk?si=qmSe4qT7Ur7zpN2W" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

For further information, refer to our [GitHub repository](https://github.com/DominikDeffner/VirtualCollectiveForaging) and our [publication in Nature Communications](https://rdcu.be/dCC3Z).

## AVHD

<div class="overview-toolbar-links">
	<a aria-label="Link to pdf" href="build/projects/avhd/detailed.html" class="no-fade"><i class="fas fa-external-link-alt"></i> <b>Project Page</b></a>
</div>


The AVHD project was designed to study how human behavior in traffic situations changes based on whether a car is controlled by another human or by an autonomous robot car.

The experiment's paradigm is simple. The participant, wearing a VR headset, is placed on one side of a street and given an incentive to reach a bus on the other side as quickly as possible without being run over. They must choose between crossing immediately, trusting that the approaching car will stop, or moving to a safe crossing point, which would constitute a detour. The experiment aims to compare decision-making when the approaching car is controlled by another participant versus when it is controlled by a computer.

In the video below, you can see the AI I programmed for the car, represented by a green/yellow/red light. The AI takes into account the player's position and trajectory, estimating the likelihood of a collision based on several parameters:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/6c4KILTMhV8?si=-Q_huBKALYPyT9Ja" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

Unfortunately, this project was shelved due to the COVID-19 pandemic, which prevented us from inviting participants and recording data.

## AutoModelCar Simulator

<div class="overview-toolbar-links">
	<a aria-label="Link to pdf" href="build/projects/automodelcar/detailed.html" class="no-fade"><i class="fas fa-external-link-alt"></i> <b>Project Page</b></a>
	<a aria-label="Link to pdf" href="https://raw.githubusercontent.com/Helliaca/AutoModelCar_Simulator/master/AutoModelCarSimulator.pdf" class="no-fade"><i class="far fa-file-pdf"></i> <b>Publication</b></a>
	<a aria-label="Link to pdf" href="https://github.com/Helliaca/AutoModelCar_Simulator" class="no-fade"><i class="fab fa-github"></i> <b>Github Page</b></a>
</div>


The AutoModelCar-Simulator is a Unity3D and ROSSharp-based simulator designed for the AutoModelCar, a miniature robot car developed at Freie Universität Berlin. The simulator allows users to run and test simple ROS nodes in a virtual environment, eliminating the need for immediate access to an actual AutoModelCar. The simulated environment closely resembles the conditions of the FU-Berlin robotics laboratory, providing a practical tool for students to develop and test their programs remotely.

![graph image](config/projects/automodelcar/pics.jpg)

Using ROSSharp and Unity, we built a sophisticated simulator that replicates the functionality of the AutoModelCar. The simulator generates camera images, LIDAR, and gyro data, closely mimicking the real-world sensors. The car's steering mechanics are based on the Ackermann model's mathematics, carefully calibrated to match the real robots' behavior.

![graph image](config/projects/automodelcar/splash.png)

We also developed a modular UI system that allows users to dynamically modify the simulation environment, akin to the real laboratory setup. Users can add, remove, or modify objects and view status and data graphs of the simulated cars. Below is a video comparison showing the same program running first on a real robot and then on a simulated one:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/0-lc6--KMSQ?si=Gzsn4BCzuQ7yuUR7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

## RTRad

<div class="overview-toolbar-links">
	<a aria-label="Link to pdf" href="build/projects/rtrad/detailed.html" class="no-fade"><i class="fas fa-external-link-alt"></i> <b>Project Page</b></a>
	<a aria-label="Link to pdf" href="https://raw.githubusercontent.com/Helliaca/RTRad/main/MT-11.pdf" class="no-fade"><i class="far fa-file-pdf"></i> <b>Publication</b></a>
	<a aria-label="Link to pdf" href="https://github.com/Helliaca/RTRad" class="no-fade"><i class="fab fa-github"></i> <b>Github Page</b></a>
</div>

RTRad was a research project completed as my Master's Thesis. It implements progressive refinement radiosity with a unique twist: it's executed entirely on the GPU and leverages Nvidia's RTX technology for visibility computations.

The program was built on Nvidia's Falcor 4.4 framework and includes a variety of useful settings, visualizations, and pre-built scenes. The underlying algorithm features numerous optimizations that I implemented, resulting in highly competitive performance compared to existing industry solutions. You can read more about these optimizations [here](https://benjamin.kahl.fi/build/projects/rtrad/detailed.html). The thesis has been cited in [several works](https://scholar.google.com/scholar?cites=14145215159720007985&as_sdt=2005&sciodt=0,5&hl=en) addressing similar topics.

The technical and mathematical details of this project are extensive, and a few paragraphs wouldn't do it justice. However, here's a brief demonstration video showcasing some of the final result's features:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/84rVIG8G1Eg?si=kXqViDNzl6OxOHtq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

## VXCT

<div class="overview-toolbar-links">
	<a aria-label="Link to pdf" href="build/projects/vxct/detailed.html" class="no-fade"><i class="fas fa-external-link-alt"></i> <b>Project Page</b></a>
	<a aria-label="Link to pdf" href="https://drive.google.com/file/d/1ZS57rgKCYl-T-sqEzVSDuj0E7VQEB6EY/view" class="no-fade"><i class="far fa-file-pdf"></i> <b>Publication</b></a>
	<a aria-label="Link to pdf" href="https://github.com/Helliaca/VXCT" class="no-fade"><i class="fab fa-github"></i> <b>Github Page</b></a>
</div>

VXCT was a computer graphics research project completed as my Bachelor's Thesis. It is an OpenGL-based implementation of the Voxel Cone Tracing algorithm for real-time indirect illumination.

The resulting program is highly customizable and includes a variety of custom software components, such as scene-serializing, displaying debug information, and setting/reading parameters in real-time through a command line.

The implementation is highly technical and complex, involving various shader mathematics. The final result was highly enlightening and performed admirably. The thesis has been cited [several times](https://scholar.google.com/scholar?cites=11457800566733753563&as_sdt=2005&sciodt=0,5&hl=en), and the corresponding [GitHub codebase](https://github.com/Helliaca/VXCT) has been forked and built upon by several other enthusiasts.

![graph image](config/projects/vxct/complex_scene.jpg)

## UnityPixelShaders

<div class="overview-toolbar-links">
	<a aria-label="Link to pdf" href="build/projects/unitypixelshaders/detailed.html" class="no-fade"><i class="fas fa-external-link-alt"></i> <b>Project Page</b></a>
</div>


UnityPixelShaders is a collection of fancy, cool looking pixel shaders I've made throughout the years. It includes many different things from raymarched fractionals to water and glass shaders. Have look below to see some examples:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Wiv5lOUgmPE?si=bKFkrZxkhwBFezGc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

## ARC-VR

<div class="overview-toolbar-links">
	<a aria-label="Link to pdf" href="build/projects/arcvr/detailed.html" class="no-fade"><i class="fas fa-external-link-alt"></i> <b>Project Page</b></a>
	<a aria-label="Link to pdf" href="https://www.vr-toolbox.org/" class="no-fade"><i class="fas fa-external-link-alt"></i> <b>Website</b></a>
	<a aria-label="Link to pdf" href="https://github.com/MPIB/arc-vr" class="no-fade"><i class="fab fa-github"></i> <b>Github Page</b></a>
</div>

ARC-VR is a Unity-based framework for developing VR cognitive studies, which I created during my tenure at the Max Planck Institute for Human Development (MPIB). It is highly modular and customizable, including components for various VR-based use cases such as locomotion, avatars, physics interactions, and more.

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/NHDEzg9Detg?si=D_PqV2vjDwW0nbJX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

I programmed all the modules and components from the ground up, using OpenXR as the only external API/library. I also held a highly praised talk on VR in cognitive science at the MPIB, where I demonstrated the capabilities of this framework:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/i877VvlbYxo?si=2_YI_iIJMZioFyqr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

## Photogammetry

<div class="overview-toolbar-links">
	<a aria-label="Link to pdf" href="build/projects/photogammetry/detailed.html" class="no-fade"><i class="fas fa-external-link-alt"></i> <b>Project Page</b></a>
</div>

As part of several different projects at the MPIB I've worked a lot with photogammetry. One of these projects consisted of producing full scans of a room's interior:

![graph image](config/projects/photogammetry/photogammetry.png)

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/8Yh81fKTSGo?si=5MBfWQeZmSkunEBC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

I've also made extensive use of life-sized 3D scanners to capture 3D models of real people, then rigged and animated them, only to place them back into reality through passthrough-VR!

<div style="display: flex; flex-direction: row;">
<img src="config/projects/photogammetry/IMG_20240626_152850.jpg" alt="image" style="height:500px;width:auto;flex:1;">
<iframe width="549" height="500" src="https://www.youtube-nocookie.com/embed/v0NtekulibU" title="VR_3dPersonScan" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="flex: 1;"></iframe>
</div>


## SDL2 Game

<div class="overview-toolbar-links">
	<a aria-label="Link to pdf" href="build/projects/sdl2_game/detailed.html" class="no-fade"><i class="fas fa-external-link-alt"></i> <b>Project Page</b></a>
</div>

Built as part of a brief university <a href="https://github.com/krother/cplusplus_abv_zedat">games with C++ workshop</a>, this simple 2D game-engine provides powerful features, including destructive terrain, rope-physics and more Fundamental ones, such as ray-casts, animations, parallax scrolling and basic physics.

Take a look at the video below to see it in action!

<p style="text-align:center;">
<iframe align="middle" width="560" height="315" src="https://www.youtube.com/embed/upb3DJJbQIM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

The underlying [codebase on github](https://github.com/Helliaca/SDL2-Game) has spawned several derivative forks and been praised for being highly educational and clear.

## Fizzo Feed 2

Fizzo Feed 2 is a personal meme-game that I made in 2016 in about 2 days as a gift/joke to a friend of mine who was notorious for his questionable performance of Fizz in the popular multiplayer game [League of Legends](https://www.leagueoflegends.com).

The game is absolutely jam-packed with insider jokes and terrible references. And, of course, it includes a highly authentic chat experience as you would find it in 2016's LoL!

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/0Gr_jcT40Qc?si=zRANi-JjeWrOX22j" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>


## CS:GO Maps

<div class="overview-toolbar-links">
	<a aria-label="Link to pdf" href="build/projects/csmaps/detailed.html" class="no-fade"><i class="fas fa-external-link-alt"></i> <b>Project Page</b></a>
	<a aria-label="Link to pdf" href="https://github.com/Helliaca/csmaps" class="no-fade"><i class="fab fa-github"></i> <b>Github Page</b></a>
</div>

I've always been a big fan of the games made by Valve, and have frequently dabbled and experimented with modding and mapping for Source-Engine games. This includes a range of CS:GO maps that range from highly detailed to complete gimmicks.

Here's an overview of some of them:

![graph image](config/projects/csmaps/de_clickspring.png)

**de_clickspring:** A bomb-defusal map with volumetric lighting and a vintage steampunk aesthetic and a plethora of self-made models.

![graph image](config/projects/csmaps/cs_research.png)

**cs_research:** A very large hostage-rescue map with rideable vehicles, many different interconnected areas and a secret easter egg!

![graph image](config/projects/csmaps/es_prison_escape.png)

**es_prison_escape:** A custom gamemode that incorporates class-based combat, procedurally changing levels and a custom win-condition. It's found a lot of favour as a 1v1 map in particular and has accumulated well over 1400 subscribers.