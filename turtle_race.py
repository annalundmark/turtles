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

finish_line = turtle.Turtle()

blue_turtle.up()
red_turtle.up()
blue_turtle.goto(-100,20)
red_turtle.goto(-100,-20)

finish_line.hideturtle()
finish_line.up()
finish_line.goto(150, -100)
finish_line.pendown()
finish_line.left(90)
finish_line.forward(200)
finish_line.up()


def set_angle_speed(): 
	turtle_angle = random.randrange(0,180)
	if turtle_angle > 90: 
		turtle_angle += 180
	turtle_speed = random.randrange(1,10)
	return turtle_angle, turtle_speed

while red_turtle.position()[0] < 150 and blue_turtle.position()[0] < 150: 
	red_turtle_angle, red_turtle_speed = set_angle_speed()
	red_turtle.setheading(red_turtle_angle)
	red_turtle.forward(red_turtle_speed)
	blue_turtle_angle, blue_turtle_speed = set_angle_speed()
	blue_turtle.setheading(blue_turtle_angle)
	blue_turtle.forward(blue_turtle_speed)


if red_turtle.position()[0] > blue_turtle.position()[0]: 
	print "Red won!" 
else: 
	print "Blue won!"


wn.exitonclick()