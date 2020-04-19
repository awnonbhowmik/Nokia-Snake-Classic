import turtle
import time
import random

delay = 0.5

# keep count of score
score = 0
high_score = 0

# setup screen
win = turtle.Screen()
win.title("Nokia Snake")
win.bgcolor("light green")
win.setup(width=600, height=600)
win.tracer(0)  # turn off screen update

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.shapesize(1)
food.color("yellow")
food.penup()
food.goto(0, 100)

segments = []

# write on screen
pen = turtle.Turtle()
pen.speed()
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Score: 0     High Score: 0", align="center",
          font=("Courier", 16, "normal"))


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


# key bindings
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")

# main game loop
while True:
    win.update()

    # check for collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear the snake
        segments.clear()

        # reset score
        score = 0

        # reset delay
        delay = 0.5

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score),
                  align="center", font=("Courier", 16, "normal"))

    # check for collision with food
    if head.distance(food) < 20:
        # move food particle to random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add body segment to snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.01

        # Increase the score
        score += 10

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score),
                  align="center", font=("Courier", 16, "normal"))

    if score > high_score:
        high_score = score

    # reverse the segment
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    # move segment 0 to the location of head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.5

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(
                score, high_score), align="center", font=("Courier", 16, "normal"))

    time.sleep(delay)

win.mainloop()
