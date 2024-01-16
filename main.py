# Turtle used for handles graphics
import turtle
import random
import time
delay = 0.1    # used in slip function of time as an argument
score = 0
highest_score = 0

# snake body
bodies = []

# getting a screen
s = turtle.Screen()
s.title("snake game")
'''s.bgpic("")     # used for set background image
s.register_shape("snake.png")
turtle.Turtle.shape("snake.png")'''
turtle.setheading(90)

s.bgcolor("grey")
s.setup(width=600, height=600)
s.tracer(0)

# create a snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()       # if turtle is moved nothing will draw
head.goto(0, 0)     # turtle moved on 0,0 means it is in center
head.direction = "stop"     # let  direction variable and its value is stopping

# create a food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()          # used for turtle not seen
food.goto(0, 200)       # initial location of food
food.st()       # square shape of food show

# create a score bord
score_bord = turtle.Turtle()
score_bord.shape("square")
score_bord.fillcolor("black")
score_bord.penup()
score_bord.hideturtle()
score_bord.ht()
score_bord.goto(-250, -250)
score_bord.write("score:0 | highest score: 0")     # this function is used for print the string message on screen

# creates a moveup function for moving th snake in all four directions
def moveup():
    if head.direction != "down":
        head.direction = "up"
def movedown():
    if head.direction != "up":
        head.direction = "down"
def moveleft():
    if head.direction != "right":
        head.direction = "left"
def moveright():
    if head.direction != "left":
        head.direction = "right"
'''def movestop():
    head.direction ="stop"'''

# this finction is used for movement mens we will do movements here of snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

# event handling  -key mapping
s.listen()
s.onkeypress(moveup, "Up")
s.onkeypress(movedown, "Down")
s.onkeypress(moveleft, "Left")
s.onkeypress(moveright, "Right")
#s.onkey(movestop, "Space")

# main loop
if __name__ == "__main__":
    while True:
        s.update()
        # check collosion with border
        if head.xcor() > 290:
            head.setx(-290)
        if head.xcor() < -290:
            head.setx(290)
        if head.ycor() > 290:
            head.sety(-290)
        if head.ycor() < -290:
            head.sety(290)

        # check collision with food
        if head.distance(food)<20:
            # move the food to new rando place
            x = random.randint(-290, 290)
            y = random.randint(-290,290)
            food.goto(x, y)

            # create a turtle for increasing the length of snake
            body = turtle.Turtle()
            body.speed(0)
            body.penup()
            body.shape("square")
            body.color("red")
            body.fillcolor("black")
            bodies.append(body)

            # increase the score
            score +=10
            # change delay
            delay -= 0.001

            # update the highest score
            if score > highest_score:
                highest_score =score
            score_bord.clear()
            score_bord.write("score: {} highest score: {}" .format(score, highest_score))
        # move the snake bodies
        for index in range(len(bodies)-1, 0, -1):
            x = bodies[index-1].xcor()
            y = bodies[index-1].ycor()
            bodies[index].goto(x, y)
        if len(bodies)>0:
            x = head.xcor()
            y = head.ycor()
            bodies[0].goto(x, y)
        move()
        # check collision with snake body
        for body in bodies:
            if body.distance(head)<20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                # hide bodies
                for body in bodies:
                    body.goto(1000,1000)
                    #body.ht()
                body.clear()

                score = 0
                delay= 0.1
                # Update scorebord
                score_bord.clear()
                score_bord.write("score: {} highest score: {}".format(score, highest_score))
        time.sleep(delay)
    s.mainloop()












