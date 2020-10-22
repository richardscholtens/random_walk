# Random walk

A program that simulates a random walk in a graphic window. It shows the way it travelled and
where the walk ended. It does so with a red circle. There is also a text shown wich tells the
end destination and how far it has travelled from the starting point. 


Assignment:

Chapter 9, assignment 13, but with a variant and with an extension. The random walk therefore starts at position (0,0) and you always have to take a step in a random direction, so that you are in (0,1), (0, -1), (1,0), or (-1 , 0) ends up. The point is to examine how far from the starting point you end up after a random walk of n steps. We use n = 1000.

NOTE: the chances of a step in each of the four directions are not equal. We take the following opportunities:

Step to the right: 0.3

Step to the left: 0.2

Step up: 0.3

Step down: 0.2

Tip: the distance from starting point (0,0) to position (x, y) is just | here x | + | y |, we don't want to be able to take oblique steps.

EXTENSION: Provide a graphical extension of this assignment, where you can see the random walk step-by-step on your screen.

Needed files:

https://mcsp.wartburg.edu/zelle/python/graphics.py

https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf
