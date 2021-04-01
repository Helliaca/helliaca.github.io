Built as part of a brief university <a href="https://github.com/krother/cplusplus_abv_zedat">games with C++ workshop</a>, this simple 2D game-engine provides powerful features, including destructive terrain, rope-physics and more Fundamental ones, such as ray-casts, animations, parallax scrolling and basic physics.

Take a look at the video below to see it in action!

<p style="text-align:center;">
<iframe align="middle" width="560" height="315" src="https://www.youtube.com/embed/upb3DJJbQIM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

Note that certain elements of the demonstration above are heavily inspired by the *Supreme Jeh'Oul* bossfight from Wings of Vi ([this one](https://www.youtube.com/watch?v=VD-y3-hH1do)).

## Architecture

The whole project is open source and within the public domain. It can be found under [this](https://github.com/Helliaca/SDL2-Game) github repository. The only dependencies are [SDL2 and SLD2-image](https://www.libsdl.org/download-2.0.php).

A highly simplified overview of the underlying engine structure can be derived from this diagram:

<img style="width: 50%;" alt="class diagram" src="config/projects/sdl2_game/class_diagram_simple.svg">

As is typical in game-engines, most entities inherit from an underlying 'Object' class that provides a function to draw them on screen as well as update them on a per-frame basis.
The *Image* class provides the visual element, whilst the *physicsObj* class provides rudimentary physics interaction such as gravity.

The *terrain* works with a bitmap on a per-pixel basis. The destructibility of any terrain pixel is given by a *terrain mask*. The terrain mask corresponding to the level in the above linked video can be seen here:

<img style="width: 50%;" alt="terrain picture" src="https://raw.githubusercontent.com/Helliaca/SDL2-Game/master/resource/terrain1_msk.png">

Note as well the purple border around the edges. Since the terrain also takes priority on the solidity of an object, this can be used to keep the player within the level's bounds.

The UML diagram below should give you a decent overview of the base classes. Keep in mind that advanced classes controlling enemies or the player are not depicted.

<img alt="class diagram" src="config/projects/sdl2_game/class_diagram.svg">

The respective source files for each class are neatly organized as follows:

### Root directory

The root directory contains what you might consider to be the 'game engine':

- *defs.h*: All constant values used across other files, including file directories, window size etc.
- *random.h*: Inline header file to generate random numbers.
- *main.cpp*: Runs the start-method in gamemaster.cpp. That's all.
- *gamemaster.cpp/.h*: Contains the base 'game-loop'. Continously clears, draws and updates all relevant objects.
- *base.cpp/.h*: Fundamental classes/functions used and inherited throughout the project. This includes: Timer, Vector2, Camera, GameWindow, Object, Image, AdvImage. Object being the base class for all Objects drawn on screen.


### Assets directory

Includes more specialized files. All of these inherit from either the Object or Image class.

- *animation*: Class for a spritesheet-animation. Used by explosion or fire aniamtions, aswells as the player sprite.
- *background*: Parallax background image that scrolls relative to player position and level size.
- *terrain*: Actual level. Pixel collision and destructible terrain are handled here.
- *missile*: The missiles that the boss spawns on his second attack.
- *physicsObj*: Base class for all physics-based Objects.
- *player*: The player.
- *projectile*: Base class for physics-based projectiles.


### assets/NAV directory

Point- and Path-classes used for the Navigation of the Boss.
Paths can have ease-in/-out aswell as linear, bezier or sine-curve interpolations.
nav_graph creates and includes preset paths for the boss to navigate along.


### assets/BOSS directory

All classes concerning the boss.

- *boss_AI*: Main wrapper for the entire thing. Looks at what attack the boss is doing and executes it by calling boss_Controller methods.
- *boss_Controller*: Handles boss idle animations, laser animations etc. Second layer of complexity wrapping.
- *boss_Head*: The main bulk of the boss' head.
- *boss_TailSegment*: The small segments that constitute the boss' tail. Each segment has an angular and positional velocity aswell as an angular and positional acceleration. At a certain self-positonal-velocity the segments will accelerate towards the vector of said velocity. If this velocity is smaller than the given threshhold, the segments will accelerate towards their default position.
- *boss_TailSegmentConnector*: The red connectors between segments.
