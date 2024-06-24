CTower is a turn-based strategy game that I am developing with a handful of friends, with myself as the lead developer.

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