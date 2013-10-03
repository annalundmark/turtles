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
start_line = turtle.Turtle()

finish_line.hideturtle()
finish_line.up()
finish_line.goto(150, -100)
finish_line.pendown()
finish_line.left(90)
finish_line.forward(200)
finish_line.up()

start_line.hideturtle()
start_line.up()
start_line.goto(-100, -100)
start_line.pendown()
start_line.left(90)
start_line.forward(200)
start_line.up()

blue_turtle.up()
red_turtle.up()
blue_turtle.goto(-100,20)
red_turtle.goto(-100,-20)

turtle_text = turtle.Turtle()
turtle_text.hideturtle()
for sec in range(3, 0, -1):
	turtle_text.write(sec, font=("Arial", 30, "normal"))
	import time
	time.sleep(1)
	turtle_text.clear()


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
	turtle_text.write("Red won!", font=("Arial", 30, "normal"))
else: 
	turtle_text.write("Blue won!", font=("Arial", 30, "normal"))


wn.exitonclick()