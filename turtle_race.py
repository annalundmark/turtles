#! /usr/bin/env python

import turtle
import random
wn = turtle.Screen()
wn.bgcolor('lightgreen')

red_turtle = turtle.Turtle()
blue_turtle = turtle.Turtle()
red_turtle.color('red')
blue_turtle.color('blue')
red_turtle.shape('turtle')
blue_turtle.shape('turtle')

blue_turtle.up()
red_turtle.up()
blue_turtle.goto(-100,20)
red_turtle.goto(-100,-20)

red_turtle_total = 0
blue_turtle_total = 0

red_turtle_angle = 0
blue_turtle_angle = 0

for etapp in range(200): 
	val = random.randrange(0,10)
	red_turtle_distance = random.randrange(1, 5)
	if val == 0: 
		red_turtle.left(90)
		red_turtle_angle += 90
	elif val == 1: 
		red_turtle.right(90)
		red_turtle_angle -= 90
	else: 
		red_turtle.forward(red_turtle_distance)
		if red_turtle_angle % 360 ==0: 
			red_turtle_total += red_turtle_distance
	val = random.randrange(0,10)
	blue_turtle_distance = random.randrange(1, 5)
	if val == 0: 
		blue_turtle.left(90)
		blue_turtle_angle += 90
	elif val == 1: 
		blue_turtle.right(90)
		blue_turtle_angle -= 90
	else: 
		blue_turtle.forward(blue_turtle_distance)
		if blue_turtle_angle % 360 ==0: 
			blue_turtle_total += blue_turtle_distance


if red_turtle_total > blue_turtle_total: 
	print "Red won!" 
else: 
	print "Blue won!"

print "Red position ", red_turtle.position()
print "Red angle ", red_turtle.heading()
print "Blue position ", blue_turtle.position()
print "Blue angle ", blue_turtle.heading()

wn.exitonclick()