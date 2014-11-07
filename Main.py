#!/usr/bin/env python3

from GameEngine_Classes import Game # Everything builds off Game()
from sys import exit

game = Game()
exit(game.main()) # game.main() returns an exit code
