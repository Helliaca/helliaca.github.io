CoinScrounge was a semi follow-up study to our ProducerScrounger experiment. Like its predecessor, it is a foraging game where players search for hidden reward patches on a field and observe whether other players have found something.
Technical Challenges

The most significant challenge in this project was configuring and programming the underlying netcode to ensure the multiplayer aspect worked reliably and smoothly. I used Unity Netcode for GameObjects, which was still in pre-release at that point, leading to numerous problems. After extensive troubleshooting, I managed to build a stable and reliable system, learning a lot in the process.

When I began the project, there was only an abstract concept with no defined aesthetic or "visual story" to grant it ecological validity. I eventually conceived the idea of players using metal detectors to search a field for coins, which I demonstrated with this basic, initial prototype:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/FcglXG6trLU?si=atoCPbjT4WEOYieN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

The project leadership approved this idea, leading us to the next challenge: player models. We aimed for realistic player models but ultimately decided on a gender-neutral design to avoid interfering with the experiment's results. We chose a basic humanoid mannequin:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/zVoNbsIJV84?si=-FCmNLIyL_QXBknU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

Another crucial aspect was signaling to other players when someone had found a reward patch. We wanted an animation to show other players that a player was digging out coins. After testing various options, we settled on a shovel excavation animation:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/6FgAhtBAEyI?si=Qt4qd4ms516aITRp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

Designing the environment was another significant task. We created many versions, each with pros and cons. Ultimately, we chose the "courtyard" version, as it was least likely to interfere with player choice, and the surrounding buildings' colors provided a simple way to highlight different experimental conditions:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/vEMAG_3U7fM?si=xMKNBLyo_oTDOpTG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

To make the experiment more interactive and engaging, we introduced a minigame where players click on appearing coins with the cursor while extracting them. To limit the effects of player skill and previous gaming experience, we significantly simplified the controls. Here is the final version:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/StMnLTMG1xk?si=qmSe4qT7Ur7zpN2W" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

The experiment also featured an extensive tutorial to introduce players to the controls and rules of the game:

<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/cCFCDHqYG_c?si=_4ZzkeZzMrmhWPcm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

For further information, refer to our [GitHub repository](https://github.com/DominikDeffner/VirtualCollectiveForaging) and our [publication in Nature Communications](https://rdcu.be/dCC3Z).