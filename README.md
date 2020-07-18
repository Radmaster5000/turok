# turok
A command line/ascii graphics dinosaur hunting game

A dumb little game written in Python to help me learn how this stupid language works.
Works okay at the minute but definitely feels over-engineered. But that's what this is for.

When I say it works okay... I basically mean it starts and ends without any obvious errors.
It's not fun.
It's not fun at all.
But it works. And it's testing my programming knowledge.

It's also helping me refresh my memory using git and GitHub.

HOW TO PLAY:

Pick a player to choose how many moves you get.

Pick a difficulty to choose how many dinosaurs are in the world.

Type 'up', 'down', 'left', and 'right' to move.

If you land on the dinosaur's space, or they land on yours, you enter a fighting minigame.

****************************************

FIGHTING MINIGAME:

Player and Dinosaur take it in turns to act.

The player options are:
* fight
* hide
* run

A roll is made to decide whether the player's action is sucessful or not. 

* fight
	* a sucessful fight roll, inflicts the player's attack damage to the dinosaur
	* an unsucessful fight roll misses. Nothing happens
* hide
	* a successful hide roll results in the player being hidden and the dinosaur having to roll to find them before attacking.
	* an unsucessful hide roll fails. Nothing happens
* run
	* breaks from the fighting minigame and returns the player to their previous position. The player may take the remainder of their moves.

The dinosaur then attempts to attack the player and a roll is made to see if they suceed. If the player is hidden, the dinosaur must roll and suceed to find them before attacking.

*******************************************

UPDATED OTHER BRANCH
