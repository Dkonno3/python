import random
import random as rnd
import turtle as ttl

screen = ttl.Screen()
screen.setup(width=500,height=500)
user_in=screen.textinput(prompt='Which turtle will win?',title='batata')
colors = ['red','blue','purple','yellow','black','orange',]
initial_y = [-40,-20,0,20,40,60]
runners = []
def set_turtle():
    for turtle in range(0,6):
        bob = ttl.Turtle(shape='turtle')
        bob.color(colors[turtle])
        bob.penup()
        bob.goto(x=-230,y=initial_y[turtle])
        runners.append(bob)
def run_forrest(runner):
    rng=rnd.randint(1,25)
    runner.forward(rng)

set_turtle()
run_prog = True
while run_prog:
    for turtle in runners:
        if turtle.xcor() > 230:
            run_prog = False
            winner = turtle.fillcolor()
            if winner == user_in:
                print(f'You won, winner is {winner}')
            else:
                print(f'You lost, the winner is {winner}')
        run_forrest(turtle)

screen.exitonclick()