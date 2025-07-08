Virtual Reality (VR) is quickly becoming a go-to tool in psychology for studying how we think and behave. It offers incredibly controlled yet dynamic environments, perfect for understanding human perception and decision-making. But there's always a big question: how well do findings from VR studies translate to the real world?

That's where sound comes in! While visuals dominate most VR experiences, our ears play a massive role in how we perceive space and immerse ourselves. Imagine being able to walk around a virtual world and hear sounds as if they were truly there, originating from specific points in the environment. This isn't just about cool effects; it's about making VR experiments even more realistic and impactful.

NOTE: If what you see here peeks your interest, make sure to have a look at the [underlying paper](https://arxiv.org/pdf/2507.03797) that goes into detail on all aspects of this project! This web-page offers just a brief summary.

## What in the World is Wave Field Synthesis (WFS)?

This project was a unique opportunity to play around with some truly cutting-edge audio technology: Wave Field Synthesis (WFS). Unlike your everyday surround sound, WFS systems use an array of loudspeakers to literally "synthesize" sound waves, making it seem like a sound is coming from a specific spot, even if there's no speaker there!

WFS is extremely rare in commercial or industry applications, but thanks to a cooperation between [Fraunhofer IDMT](https://www.idmt.fraunhofer.de/) and the Max-Planck Institute for Human Development (MPIB), I had the rare opportunity to play around with this tech and build a VR experience offering unparalleled sound rendering!

## The Setup

To bring this project to life, I had the incredible opportunity to work with some serious, high-end equipment. As you might expect, cutting edge, research-oriented tech comes with a respective amount of *jank*. And yes, indeed, the hardware and software did not always cooperate to the extent I would have liked, but such are the chores of charting the unexplored!

The heart of the project was a custom-built Wave Field Synthesis system at the Max Planck Institute for Human Development (MPIB), developed by Fraunhofer IDMT. Imagine a sound-isolated room with a square array of 64 speakers (16 on each side!), all working together to create a 2x2 meter "sweet spot" where you can experience perfectly localized sound:

![graph](config/projects/wfs_vr/res/IMG_20240325_144601.jpg)

Getting sounds into this system involved a dedicated rendering PC, hooked up via a special USB audio interface. For real-time control, I sent commands from our VR application to the WFS system over a network, letting me pinpoint exactly where a sound should appear in the room.

Building this all required a blend of specialized software. I used Unity 2021 as my primary development environment. Most of the core VR components were built using ARC-VR, an in-house framework, developed by yours truly, at MPIB specifically for VR research.

For voice instructions during the study, I leveraged ElevenLabs to generate natural-sounding voiceovers, and even built a custom Unity plugin to streamline that process. Switching between the WFS system and the stereo headphones for different parts of the experiment was handled by SVCL, a handy command-line tool.

## Too Many Prototype

My journey into combining WFS and VR kicked off with a simple prototype. The idea was to test the waters: could we actually use WFS in a VR environment for a sound localization task? The initial feedback was great – people found it fun and engaging! However, it quickly became clear that this first version, while cool, wasn't quite robust enough for serious scientific study. For instance, participants were limited to picking from a fixed number of phones in a virtual bar, which meant even if their hearing wasn't perfectly accurate, they could still guess correctly by chance. This "noise" in the data meant I needed a more precise way to measure how well people could pinpoint sounds.

![graph](config/projects/wfs_vr/res/first_proto_selection.png)

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/CWmqsejxNqI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

This led me down a path of creating several different prototypes, each designed to tackle the challenge of accurately measuring sound localization. I experimented with various ways for participants to interact with the virtual sound sources:

- "Phone-Placement": Here, participants would "grab" a virtual phone with their controller and place it exactly where they thought the sound came from. This was intuitive, but it meant sounds (and guesses) were limited to the physical WFS space.
- "Dot-Circle": This version was more abstract. Participants would select a dot on a virtual circle around them, indicating the direction of the sound. This allowed for sounds outside the WFS area, but didn't account for "depth."
- "Laser-Pointer": This gave participants a virtual laser to point at a "canvas" in the virtual space, offering the highest resolution for placing a sound source. The downside was that accuracy could be affected by how far away they were pointing, and the placement plane could feel a bit unintuitive.
- "Volume-Selection": Building on the phone-placement idea, this allowed participants to select a specific 3D volume from a grid where they thought the sound originated. While interesting, finding the "right" size of volume was tricky and could obstruct their view.

![graph](config/projects/wfs_vr/res/prototypes.png)

This is, arguably, *too many* prototypes. A common swamp I find myself stuck in. I don't like to leave any stone unturned...

However, this extensive prototyping phase gave me some solid insight into the unique challenges of leveraging WFS alongside VR. If you're interested in reading about some of the limitations and challenges I encountered, be sure to refer to the project's [underlying paper](https://arxiv.org/pdf/2507.03797)!

## Bringing It All Together

After a lot of prototyping and learning, I finally built the definitive version of the experiment for data collection. This version took the best elements from the earlier trials, especially the intuitive "phone-placement" interaction, and added a whole lot more to make it a truly comprehensive study.

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/YAaiDir7U2g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

In this final setup, participants were still tasked with pinpointing the origin of sounds within that 2x2 meter WFS sweet spot. The big upgrade? They now used hand-tracking (or controllers as a backup) to make their guess by simply pinching their fingers at the perceived sound location. This felt incredibly natural and immersive.

![graph](config/projects/wfs_vr/res/trial.png)

### The Conditions: Sounds, Environments, and Movement

To really dig into how different factors influence sound localization, I introduced a variety of conditions:

- Sounds: We used three distinct sounds: a classic rotary phone ring, a short piano melody, and a chirping bird. Each had different characteristics in terms of length and frequency.
- Environments: To see if the visual surroundings played a role, I created three virtual environments designed to match the sounds: a neutral, checkered room; an indoor bar; and a vast outdoor mountain village.
- Static vs. Dynamic Sounds: Participants first completed "static trials" where the sound stayed in one place. Then, they moved on to "dynamic trials" where the sound source actually moved along a trajectory before stopping, testing how well they could track moving audio.

![graph](config/projects/wfs_vr/res/envs_v2.png)

Each participant went through 54 trials in total, experiencing both WFS and stereo headphone playback across all these conditions. It usually took about 25-35 minutes to complete.

### Making it User-Friendly: Tutorials and Calibration

One thing I'm particularly proud of is how user-friendly this project became. I spent a lot of time building an extensive interactive tutorial. Narrated by AI-generated voices, it guided participants step-by-step through how to interact with the system, how to make their guesses, and what to expect during the experiment. It even covered safety aspects and how to pause if they felt uncomfortable. This made it one of the most accessible VR experiences I've ever built!

Another crucial element was spatial calibration. Because the Meta Quest Pro is a mobile headset, its exact position in the real world could vary slightly each session. This meant the virtual environment might not perfectly align with the physical WFS sound field. To fix this, I implemented a clever calibration step: using the Quest Pro's passthrough camera, the experimenter could see the real room overlaid with a virtual grid. They could then use the VR controllers to precisely align the virtual and real WFS spaces, ensuring that what participants saw visually matched what they heard acoustically.

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/668u1TINfV0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

Finally, I built in experimenter controls that allowed me to monitor the participant's view in real-time, track their progress, and even pause the experiment if needed. This ensured a smooth and controlled data collection process.

## Results

So, after all that development and data collection, what did we find out?

Surprisingly, when it came to sheer accuracy, the good old stereo headphones, especially with a really steep volume falloff, actually performed better than the WFS system. Participants tended to take a bit longer with stereo, but their final guesses were often closer to the true sound source. This was particularly noticeable for stationary sounds.

![graph](config/projects/wfs_vr/res/scores_base.png)

However, many participants felt that the WFS system delivered a far more natural and immersive sound experience. It gave them an immediate, intuitive sense of where the sound was coming from, even if their final pinpoint wasn't as precise as with stereo. Very steep falloffs do not sound or feel natural, as sounds can travel very far in usual real-life conditions.

A key takeaway was the impact of "user-dependent optimization" on WFS. Our system didn't account for the listener's exact position in the room, and this showed in the results: participants' guesses with WFS tended to gravitate towards the edges of the listening area, especially for sounds originating from the center. This isn't a flaw of WFS itself, but rather highlights the importance of incorporating real-time user tracking into these systems for optimal performance. (For a deep dive into this, check out the full paper!)

![graph](config/projects/wfs_vr/res/trial_tracked_v1.png)

This project provided invaluable insights into the potential and challenges of using WFS in VR for psychological research. If you're keen on all the nitty-gritty details, including the specific data and statistical analysis, you can dive into the full paper!
