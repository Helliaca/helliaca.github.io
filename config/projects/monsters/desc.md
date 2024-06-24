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