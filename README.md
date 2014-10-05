Idiot Rewrite
=============

**Philosophies**
* Only pass iterables of Card instances rather than just instances
* Make game control flow as understandable as possible by abstracting to verbosely-named functions
* Make game control function scope as logical as possible (e.g. play\_from\_faceups in Player class, no pickup\_func in Pile class)

**Tasks**
* Game Engine class: Game which will control and progress game state
* Game Engine classes: Human, Cpu which call respective gameplay functions
* Game Engine functions for Human which call interface functions
* Game Engine functions for Cpu (AI) which call interface functions
* Interface functions (first cli, then graphical)

**Completed**
* Game Engine classes: Card, Deck, Pile, Three

**Graphics**
* Gather/create static files
* Gameframe
* Upgrade functions and objects
