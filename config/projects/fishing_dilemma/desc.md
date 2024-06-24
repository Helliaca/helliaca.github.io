The Fisher's Dilemma is a foraging study I developed at the [Max-Planck Institute for Human Development](https://www.mpib-berlin.mpg.de/en). Its goal is to examine how people utilize social information to forage for resources and how their behavior shifts between cooperative and competitive environments.

The core gameplay is remarkably straightforward: Players fish from several ponds, and the analysis focuses on how long it takes them to find the optimal pond and the extent to which observing other players influences their decisions.

Here’s a demonstration video of how it looks:

[ -- COMING SOON -- ]

A major challenge in this project was the multiplayer aspect and the underlying net code. Instead of relying on existing networking libraries, I decided to push my boundaries and develop a completely new, self-made net code library specifically for this project.

This library, which I named HNetwork, functions as a client-agnostic, network-synchronized Dictionary that holds the current game state. Clients interpret and render this state for each player. Synchronization is managed through a combination of TCP and UDP packets, using self-written serializers to ensure efficient communication.

The experiment shown above represents the second iteration of this concept. The previous version was significantly simpler, featuring only two ponds and allowing players to switch ponds instantaneously.

Here’s an image of the earlier version:

![graph](config/fishing_dilemma/splash.png)