import turtle
import random
import time

# Screen
delay = 0.1
score = 0
high_score = 0
bodies = []

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.fillcolor("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.fillcolor("blue")
food.penup()
food.goto(100, 100)

# Score Board
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(
    "Score: 0   High Score: 0",
    align="center",
    font=("Arial", 16, "bold")
)

# Snake Movement Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def moveStop():
    head.direction='stop'

def move():
    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        head.sety(y + 20)

    elif head.direction == "down":
        head.sety(y - 20)

    elif head.direction == "left":
        head.setx(x - 20)

    elif head.direction == "right":
        head.setx(x + 20)

# Keyboard
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
screen.onkeypress(moveStop,'space')

# Main Game Loop
while True:
    screen.update()

    # Border Wrap
    if head.xcor() > 290:
        head.setx(-290)

    if head.xcor() < -290:
        head.setx(290)

    if head.ycor() > 290:
        head.sety(-290)

    if head.ycor() < -290:
        head.sety(290)

    # Food Collision
    if head.distance(food) < 20:

        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("green")
        body.penup()
        bodies.append(body)

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(
            f"Score: {score}   High Score: {high_score}",
            align="center",
            font=("Arial", 16, "bold")
        )

        if delay > 0.05:
            delay -= 0.001

    # Move Body
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        bodies[0].goto(head.xcor(), head.ycor())

    move()

    # Body Collision
    for body in bodies:
        if body.distance(head) < 20:

            time.sleep(1)

            head.goto(0, 0)
            head.direction = "stop"

            for segment in bodies:
                segment.goto(1000, 1000)

            bodies.clear()

            score = 0
            delay = 0.1

            pen.clear()
            pen.write(
                f"Score: {score}   High Score: {high_score}",
                align="center",
                font=("Arial", 16, "bold")
            )

    time.sleep(delay)