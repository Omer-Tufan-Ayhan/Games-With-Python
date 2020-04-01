import turtle
import random

score = 0
lives = 3

wn = turtle.Screen()
wn.title("Fallinng Skies by OTA")
wn.bgcolor("green")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# Add the player 
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# Add the pen 
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(-200, 260)
font = ("courier", 24, "normal")
pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=font)

# Create a list of good guys
good_guys = []

# Add the good_guys
for x in range(20):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("circle")
    good_guy.color("blue")
    good_guy.penup()
    good_guy.goto(-100, 250)
    good_guy.speed = random.randint(1, 2)
    good_guys.append(good_guy)

# Create a list of good guys
bad_guys = []

# Add the bad_guys
for x in range(20):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("circle")
    bad_guy.color("red")
    bad_guy.penup()
    bad_guy.goto(100, 250)
    bad_guy.speed = random.randint(1, 2)
    bad_guys.append(bad_guy)

# Functions
def go_left():
    player.direction = "left"

def go_right():
    player.direction = "right"

# Keyboard bindings
wn.listen()
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    # Update screen
    wn.update()

    # Move the player 
    if player.direction == "left":
         x = player.xcor()
         x -=1
         player.setx(x)

    if player.direction == "right":
         x = player.xcor()
         x +=1
         player.setx(x)
    
    # Move the good guys
    for good_guy in good_guys:
        y = good_guy.ycor()
        y -= good_guy.speed
        good_guy.sety(y)

        # Check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 350)
            good_guy.goto(x, y)

        # Check for a collision with player
        if good_guy.distance(player) < 20 :
            x = random.randint(-380, 380)
            y = random.randint(300, 350)
            good_guy.goto(x, y)
            score +=10
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=font)
        
    # Move the bad guys
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)

        # Check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 350)
            bad_guy.goto(x, y) 

        # Check for a collision with the player
        if bad_guy.distance(player) < 20 :
            x = random.randint(-380, 380)
            y = random.randint(300, 350)
            bad_guy.goto(x, y)
            score -=10
            lives -= 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=font)
            
        if lives < 1 :
            player.hideturtle()
            bad_guy.hideturle()
            good_guy.hideturtle()
            print("GAME OVER")
            break

wn.mainloop()    
