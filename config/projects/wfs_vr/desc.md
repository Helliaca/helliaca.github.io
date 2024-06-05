# Integration of WFS Spatial Audio with Unity VR Projects

# 1 Premise

Wave field synthesis (WFS) is an audio rendering technique that creates virtual acoustic environments by
simulating sound waves. Loudspeaker arrays synthesize artificial wavefronts that seem to originate from a
given start-point by super-imposing a large set of individual, elementary sound-waves.

Such systems have the potential to provide an unprecedented amount of immersion for behavioral studies
that are audio-sensitive and utilize VR.

Due to their high cost, complexity and sensitivity to room acoustics, WFS systems are hitherto seldom used
and have not yet reached market maturity. This novelty and limited accessibility opens up a new front of
research thus far untrodden in the field of psychology.

Unlike commonly available, software-based spatial audio solutions such asSteam Audio^1 orDolby Atmos^2 ,
WFS-based systems do not rely on HRTFs. As such, WFS systems are agnostic to the listener and
circumvent the inter-subject variability that inhibit the reliability of HRTF-based systems^3 in behavioural
studies.

## 1.1 Goals

As an initial stepping-stone, we seek to combine WFS into a simple VR-based experiment that measures
how accurately participants perceive the origin-points of artificial wavefronts. Further points of interest
include (but are not limited to) which factors affect localization-accuracy, which advantages and limitations
WFS systems have over their more accessible counterparts, and which type of studies would benefit most
from it’s integration.

## 1.2 WFS Setup

The employed WFS setup consists of four arrays of 16 loudspeakers each, arranged into a square with
a surface area of 2×2m. Inside this area the participant can move around freely and hear the virtual
sounds-sources.

All speakers are at the same height, thus only allowing the spatial rendering to be done on a XZ-plane at
this height.

They are complemented by 3 subwoofers positioned on the ground.

(^1) https://valvesoftware.github.io/steam-audio/
(^2) https://www.dolby.com/technologies/dolby-atmos/
(^3) https://pubmed.ncbi.nlm.nih.gov/20496243/


Figure 1:The employed WFS setup. The area marked in black tape corresponds to the WFS-area the participant
can move around in.

Figure 2:Difference between WFS-space and virtual-space: Whilst the participant can only move around and hear
the artificial wave-fronts inside a 2×2m area, the size of the virtual environment (where virtual objects sound sources
can be placed) extends far beyond.


# 2 Initial Prototype

As a first step, a simple prototype was assembled that takes the form of a simple task where the participant
is placed into a virtual environment (resembling a bar) of 10×10m with a series of telephones placed
arbitrarily at various locations inside.

Every 3-10 seconds, one of the phones emits a ringing sound, and the participant is prompted to select the
phone they believe to have rung using a virtual ’laser-pointer’.

If the selected phone was the correct one, it disappears. The trial ends once no phones are left inside the
room.

Figure 3:Participant in virtual space (visualized by a robot) pointing out a phone. Third person view (left) and
first-person view (right).

Figure 4:Participant inside the WFS system selecting a phone. The VR view is streamed over WIFI to aMeta
Quest Proheadset and presented to the participant. For a full video-demonstration, refer to the following link:
https://www.youtube.com/watch?v=CWmqsejxNqI.


## 2.1 Technology

The prototype was build usingUnity 2021.3.17, usingextOSC^4 to communicate with the WFS-renderer’s
OSC interface. Most of the VR components of the prototype were put together using the in-house built
ARC-VR^5 framework.

For individual sound-sources (as is the case with this experiment), extOSC provides a remarkably seamless
and straight-forwards integration of the WFS system. Requiring multiple simultaneous audio-sources may
complicate the procedure and has, thus far, not been tested or implemented.

## 2.2 WFS-related Problems and Limitations

2.2.1 Auditory Depth-Perception

Early testing of this prototype indicated that the direction of a ringing phone’s location was highly percepti-
ble, but that it’s distance was not. For multiple sound-sources placed along a line originating at the listener,
it became difficult to distinguish one from the other. Possibly due to a lack of volume-attenuation.

Generally, going beyond a count of 10+ phones increased the difficulty of the task substantially.

2.2.2 Lack of Height Localization

The underlying WFS setup can only produce wavefronts on a plane at the height of the speaker-array. Since
the prototype places phones at varying heights (both above and below the height of the speaker-array)
there is a steady miss-match in the sound origins and visual models.

Put simply, the ring of a phone located on a shelf does not necessarily sound like it is coming from above,
nor does a phone located on a table sound like is coming from below.

2.2.3 Lack of Occlusion

The WFS renderer is agnostic to any obstacles located in the virtual environment that a participant might
expect to dampen or obfuscate sounds. For instance, ducking behind the bar-counter does not affect sound
clarity at all. Room acoustics in general do not conform to those the virtual space would entail and may
require an additional step of sound-processing.

As such, the present experiment is only adequate for sound-sources that are in the direct line-of-view of
the participant and that would not be expected to create echoes or indirect sound-waves.

2.2.4 Limited Space

Because of the above described depth-perception challenge, moving around the virtual space proved highly
beneficial in locating a phone’s position, due to the auditory parallax-effect that would take place whilst
moving.

(^4) https://github.com/Iam1337/extOSC
(^5) https://github.com/MPIB/arc-vr


Figure 5:Hypothetical example of a sound being dampened by an occluder. Obstacles surface echoes are not
simulated by the WFS renderer.

Figure 6:Benefits of moving around the virtual space: The change in direction of a distant phone is lesser than that
of a closer one, giving an indication of depth/distance.

The employed WFS setup only provides a small area for movement, which furthermore limits the possibilities
of phones being placed inside the virtual space that overlaps the WFS-space (most were placed outside, in
the pure virtual space).


2.2.5 Lining up Virtual-Space and WFS-space

Since the WFS renderer and VR application are separate, there are some challenges in lining up the visual
virtual space of the VR headset with the audio virtual-space of the WFS system.

The prototype includes a calibration step at the beginning prompting the participant to stand at the center
of the WFS-space and look in a certain direction to line up the origin and rotation of both spaces.

Such a manual calibration can introduce inaccuracies as the VR headset’s location and rotation will always
be at least somewhat imperfect and may vary based on each calibration.

Figure 7:Participant in virtual space (represented by a robot) presented with pre-trial calibration step. By standing
in the center of the WFS-space and looking at in the given direction, the virtual spaces are lined up.

## 2.3 Concept Limitations

The design of the underlying experiment comes with some rather glaring limitations.

Most obvious of these is the nature of only providing the participant a limited number of phones (and thus
locations) to choose from.

As such, the accuracy of sound localization could be very poor, and a participant would still be able to
select the correct one if only two options are available (out of random chance, or rough hints from the
localization), whilst the localization could also be superb, but a participant would still likely select the
wrong option if the room includes a large number of phones.

This arbitrary limitations pollutes any qualitative measurement for accuracy.

# 3 Improved Prototypes

As a follow-up to the initial prototype, we devised a set of three re-designs that, hopefully, allow for a reliable
measurement of an euclidean-distancedelta-valuebetween the location the participant perceives/indicates,
and the location that the wavefront was actually created at.


## 3.1 Phone-Placement Version

In this variant, the participant does notchooseone of several options, but instead points out the location
they believe the sound to have originated from directly.

After a ring is sounded, the participant’s VR controller is given a ’virtual phone’ which they can move and
place into a desired location using the controller’s trigger button.

Figure 8:The participant in virtual space, represented by robot, placing a virtual phone at the location of the
perceived sound. Third-person view (left) and from first-person view (right)

Notes/Observations:

- Due to being tied to the exact location of a participant’s hand/controller, phones cannot not be
    placed outside of the limited WFS-space, thus all sounds have to originate from within as well.
- The participant can place phones above or below the height of the speakers, even though the current
    WFS system can only localize sounds at one height.
- This version provides the most intuitive and simple controls for inexperienced VR users, the most
    accurate placement, but is severely constrained by being able to only place sound-sources inside of
    the WFS-space.
- This variant opens up the possibility of using a VR-tracked, 3D-printed phone to give the participants
    to place for increased ecological validity.

## 3.2 Dot-Circle Version

In this variant the participant is provided an array of dots in a circle at head-height around the center of
the WFS-space, of which they can select the one they believed to be closest to the sound’s origin.

Observations:

- This more abstract variant makes no reference at all to ’telephones’. Whilst less immersive, it could
    thus work better with entirely different sounds.
- Adjusting the delta-angle of the placed dots to choose from allows for the measurement of an average
    distance/angle at which the accuracy of localization begins to vein. (Imagine a series of trials where
    the density of dots increases/decreases with each one).


Figure 9:The participant in virtual space, represented by robot, pointing out the sound’s location from a circle of
options. Third-person view (left) and from first-person view (right)

- This version allows sounds to originate from outside the WFS area, but since all the dots are located
    on a circle around the room’s center, the participant does not indicate the ’depth’ at which the sound
    originated from, only the direction. A depth-selection would either require one of the other variants,
    or limiting the phone-distance to a single value per trial.
- Since the primary input parameter is measured as anangleinstead of a distance, this variant would
    provide a counter-balance to the expected inverse-square decrease in accuracy.
- This variant dis-incentivizes the participant from moving around the virtual space, as the parallax-
    effect is no longer as useful.

## 3.3 Laser-Pointer

In this variant, the participant can point out a location on a virtual ’canvas’ at head-height by using a
virtual laser-pointer.

Figure 10:The participant in virtual space, represented by robot, pointing out the sound’s location on the selection-
canvas from a third-person view (left) and from first-person view (right)

Observations:

- This variant allows participants to both place phones inside and outside the WFS area. As such, it
    provides the highest resolution/options for positions out of all tested versions.


- The accuracy of a selected location scales to inverse square of the distance between the participant
    and the location and thus leads to a natural increase in the expected delta-values. In other words,
    noise from tracking inaccuracies or the participant’s hand movements are amplified the larger the
    selected location is, due to the increased length of the laser-ray.
- Having a laser-canvas on the XZ-plane at head-height isn’t the most intuitive system and can provide
    an accuracy advantage to participants that duck or crouch.
- The selection plane being close to eye-height can make it difficult to see and select a location. A
    conceivable solution would be to move the selection plane up or down from the actual height of the
    speakers.

# 4 Further Considerations

## 4.1 Laser-Pointer Grid-array

One possible option to ameliorate the issues of the Laser-Pointer version would be to combine it with the
Dot-Circle version. Essentially, having the pointer snap to given points on a grid, thus reducing (if not
eliminating) the noise from distance-based inaccuracy in selection.

## 4.2 Variation Ringing Sounds

In the current version, the ring-sound employed is always identical. It seems prudent to employ different
sounds, or variations in pitch and frequency.

## 4.3 Background Noise

The sound that needs to be located is currently the only sound-source that is being employed. One possible
avenue of interest could be to measure the influence of additional sound-sources on localization accuracy.


