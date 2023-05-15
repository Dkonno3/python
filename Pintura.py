import random
import colorgram
import turtle as ttl
bob = ttl.Turtle()
screen = ttl.Screen()
ttl.colormode(255)
rgb_colors = []
colors = colorgram.extract('image.jpg', 50)
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]
#screen.window_width(640)
#screen.window_height(480)
bob.speed(0)
def paint_dot():
    bob.dot(20, random.choice(color_list))
    bob.penup()
    bob.forward(40)
    bob.pendown()
def turn_left():
    bob.dot(20, random.choice(color_list))
    bob.left(90)
    bob.up()
    bob.forward(40)
    bob.left(90)
def turn_right():
    bob.dot(20, random.choice(color_list))
    bob.right(90)
    bob.up()
    bob.forward(40)
    bob.right(90)
def reset_bob():
    bob.penup()
    bob.setx(-460)
    bob.sety(-380)
reset_bob()
bob.hideturtle()
run = True
while run:
    if bob.xcor() < 450:
        while bob.xcor() <= 450:
            paint_dot()
            print(bob.position())
        turn_left()
    if bob.xcor() > -450:
        while bob.xcor() >= -450:
            paint_dot()
            print(bob.position())
        turn_right()
    if bob.xcor() <= -450 and bob.ycor() >= 380 :
        run = False
screen.exitonclick()