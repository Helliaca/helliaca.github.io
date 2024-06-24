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