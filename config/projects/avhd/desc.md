The AVHD project was designed to study how human behavior in traffic situations changes based on whether a car is controlled by another human or by an autonomous robot car.

The experiment's paradigm is simple. The participant, wearing a VR headset, is placed on one side of a street and given an incentive to reach a bus on the other side as quickly as possible without being run over. They must choose between crossing immediately, trusting that the approaching car will stop, or moving to a safe crossing point, which would constitute a detour. The experiment aims to compare decision-making when the approaching car is controlled by another participant versus when it is controlled by a computer:

![graph image](config/projects/avhd/paradigm.png)

Initially, I built an environment with a two-way street and cars moving at high speed:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/1wq6776S-Qc?si=znuQXnFnhKhSkUAC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

We eventually concluded that we didn't have enough real-world space for a setup where the participant could cross a double street. Thus, we scaled it back to a single street, featuring a dense convoy of cars followed by a significant gap and then the target car. In the video below, you can see the AI I programmed for the car, represented by a green/yellow/red light. The AI takes into account the player's position and trajectory, estimating the likelihood of a collision based on several parameters:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/6c4KILTMhV8?si=-Q_huBKALYPyT9Ja" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

Unfortunately, this project was shelved due to the COVID-19 pandemic, which prevented us from inviting participants and recording data. It has not been revived since.