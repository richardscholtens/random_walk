#!/usr/bin/python3
#student: Richard J.F.P. Scholtens
#studentnr.: s2956586
#datum: 06/12/2016
"""
A program that simulates a random walk in a graphic window. It shows the way it travelled and
where the walk ended. It does so with a red circle. There is also a text shown wich tells the
end destination and how far it has travelled from the starting point. 
"""


from random import randrange
from graphics import *
from time import sleep

def simulate_random_step(x, y):
	"""A function that simulates a random step and returns 
	a number for deciding which way it the step went."""
	random_counter = randrange(0,10)
	if random_counter <= 6:
		if random_counter <= 3:
			if random_counter <= 1:				#20% chance left
				x = x - 1
				return (Point(x,y), 0)
			else:								#20% chance down
				y = y - 1
				return (Point(x,y), 1)
	else:										#30% chance right
		x = x + 1
		return (Point(x,y), 2)

	y = y + 1										#30% chance up
	return (Point(x,y), 3)


def draws_circle(position, color, win):
	"""A function that draws a red circle."""
	center = position
	circle = Circle(center, 0.75)
	circle.setFill(color)
	circle.draw(win)

def draws_line(point1, point2, color, win):
	"""A function that draws a line."""
	line = Line(point1, point2)
	line.setFill(color)
	line.setWidth(5)
	line.draw(win)

def draws_text(point, text, win):
	"""A function that draws a text."""
	text = Text(point, text)
	text.draw(win)

def coords_checker(point, coords, win):
	"""A function which checks if the coords of the window are big enough. 
	If it is not big enough it will change the coords accordingly."""
	if point.getX() == coords[0] or point.getY() == coords[1]:
		coords[0] -= 3
		coords[1] -= 3
		win.setCoords(coords[0], coords[1], coords[2], coords[3])

	elif point.getX() == coords[2] or point.getY() == coords[3]:
		coords[2] += 3
		coords[3] += 3
		win.setCoords(coords[0], coords[1], coords[2], coords[3])
	
	return coords

def center_x(coords):
	"""Determines the center X axle of the window."""
	return int((coords[0] + coords[2])/2)


def main():
	simulated_steps = 1000
	x = y = best_x = best_y = 0 
	previous_point = Point(x,y)
	win = GraphWin("Random Walk",500,500)
	win.setCoords(-1, -1, 1, 1)
	coords = [-1,-1,1,1]
	colors = ["blue", "orange", "brown", "purple", "green", "red"]


	for i in range(simulated_steps):
		point, number = simulate_random_step(x,y)
		coords = coords_checker(point, coords, win)
		draws_line(previous_point, point, colors[number], win)
		previous_point = point
		x = point.getX()
		y = point.getY()
		time.sleep(0.1)
	
	center = center_x(coords)
	draws_circle(Point(0,0), colors[4], win)	
	draws_circle(point, colors[5], win)
	win.setCoords(coords[0] - 15, coords[1], coords[2] + 15, coords[3] + 30 )
	draws_text(Point(center, coords[3] + 15), "Your last random step was on X {0} and Y {1}.".format(int(x),int(y),),win)
	draws_text(Point(center, coords[3] +10), "This means you have moved a total of {0} steps.".format(int(abs(x)+abs(y))),win)
	
	win.getMouse()
	win.close()
if (__name__ == '__main__'):
	main()

