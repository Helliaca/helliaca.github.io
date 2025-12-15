---

Development of this software has been kindly supported by

- [Prof. Dr. Dirk Richter](https://www.uni-potsdam.de/de/erziehungswissenschaftliche-bildungsforschung/prof-dr-dirk-richter) (Professorship of Educational Research in the Educational Sciences, University of Potsdam), in collaboration with
- [Prof. Dr. Yizhen Huang](https://uni-tuebingen.de/en/faculties/faculty-of-economics-and-social-sciences/subjects/department-of-social-sciences/education-sciences-and-psychology/institute/staff/huang-yizhen/) (Junior Professor of Education Sciences and Psychology, University of Tübingen) and 
- [Prof. Dr. Eric Richter](https://www.ku.de/ppf/paedagogik/lehrstuehle-professuren/ppf/paedagogik/lehrstuhl-fuer-schulpaedagogik/mitarbeitende/prof-dr-eric-richter) (Professorship of School Pedagogy, Catholic University of EichstaettIngolstadt)

DigiProMIN, a BMBFSFJ (Federal Ministry for Education, Family Affairs, Senior Citizens, Women and Youth) funded project

---




## Project Overview

While the **VR Classroom** project existed prior to my involvement, it initially faced significant challenges regarding stability and performance. I was originally contracted by the University of Potsdam to address these bottlenecks and optimize the existing framework.

However, as development progressed, the scope expanded into a comprehensive modernization of the application. I ended up overhauling the majority of the project's systems to ensure scalability and robustness, to the extent that very little of the original legacy codebase remains. Beyond the backend logic, I also implemented a significant upgrade to the visual fidelity to increase the immersion required for effective psychological research.

![Screenshot of the VR Classroom visual upgrade](config/projects/vr-classroom/before_after_screenshot.jpg)

### AI-Driven Interaction

The most transformative feature I engineered was the full integration of Generative AI. Previously, interaction was limited, but the new system now allows teacher trainees to interact naturally with students using their voice.

By integrating a pipeline of **Speech-to-Text (STT)**, **Large Language Models (LLMs)**, and **Text-to-Speech (TTS)**, the virtual students can now listen, understand, and verbally respond to the user in real-time. This creates a high-fidelity training environment where "classroom management" is no longer a button press, but a conversation.

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/y2HbNZqD4rI?si=_w9DoZZIamf6FmSl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>


### Key Features & Mechanics

Beyond the core AI conversation loop, I implemented several systems designed to support the pedagogical goals of the project:

* **Student Attention System:** A dynamic system that governs student behavior. The "Attention" value directly drives procedural animations, causing students to look around, fidget, or focus on the teacher based on their engagement level.
* **Interactive Tutorial:** To lower the barrier to entry for non-technical users, I built a fully voiced, interactive tutorial that guides new users through the VR controls.
* **Post-Session Analysis:** Education research relies on data. I built a comprehensive analysis dashboard that provides trainees with feedback on their performance, offering insights into their speaking time, gaze, and class engagement.

![Screenshot of the post-session analysis dashboard](config/projects/vr-classroom/collage.png)

### Current Status

The project has made great strides and is currently in active deployment, having already been utilized in several sessions with real teachers-in-training.

Development is ongoing, with a current focus on porting features to non-VR versions to increase accessibility. I am excited to continue expanding the capabilities of this tool and helping the University of Potsdam push the boundaries of digital education.