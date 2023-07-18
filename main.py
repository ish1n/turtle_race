from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make bet", prompt="choice which player will win :")
colors = ["red", "orange", "green", "blue", "yellow"]
y = [-100, -50, 0, 50, 100]
num_of_turtle = 5
turtles = []

# ishan = [Turtle(shape="turtle") for i in range(5)].
# y= -100
#
# for pos in range(0,5):
#
#
#     ishan[pos].goto(-230,y)
#     y=y+50


# ishan.goto(-230,0)

for i in range(0, 5):
    ishan = Turtle(shape="turtle")
    ishan.penup()
    ishan.goto(-230, y[i])
    ishan.color(colors[i])
    turtles.append(ishan)
if user_bet:
    is_race_on = True
while is_race_on:

    for i in turtles:
        if i.xcor() > 230:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print(f"you won {winning_color}  color turtle won")
            else:
                print(f"you lost ,this color {winning_color} won")
        random_dist = random.randint(0, 10)
        i.fd(random_dist)

screen.exitonclick()
