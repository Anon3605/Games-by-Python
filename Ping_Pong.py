import turtle
import time
import winsound

window=turtle.Screen()
window.title("Pong game")
window.bgcolor("Green")
window.setup(width=1366, height=720)
window.tracer(0)

def padd_Aup():
    y=padd_a.ycor()
    y+=20
    padd_a.sety(y)

def padd_Adown():
    y=padd_a.ycor()
    y-=20
    padd_a.sety(y)

def padd_Bup():
    y=padd_b.ycor()
    y+=20
    padd_b.sety(y)

def padd_Bdown():
    y=padd_b.ycor()
    y-=20
    padd_b.sety(y)

# Paddle A
padd_a=turtle.Turtle()
padd_a.speed(0)
padd_a.shape("square")
padd_a.shapesize(stretch_wid=5,stretch_len=1)
padd_a.color("Black")
padd_a.penup()
padd_a.goto(-600,0)


# Paddle B
padd_b=turtle.Turtle()
padd_b.speed(0)
padd_b.shape("square")
padd_b.shapesize(stretch_wid=5,stretch_len=1)
padd_b.color("Black")
padd_b.penup()
padd_b.goto(600,0)


#Keyboard binding
window.listen()
window.onkeypress(padd_Aup, "w")
window.onkeypress(padd_Adown, "s")
window.onkeypress(padd_Bup, "5")
window.onkeypress(padd_Bdown, "2")

#Score
score_a = 0
score_b = 0

#Ball
ball=turtle.Turtle()
ball.shape("circle")
ball.color("Black")
ball.penup()
ball.goto(0,0)
ball.dx=1
ball.dy=1

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("Black")
pen.hideturtle()
pen.goto(0,300)
pen.write(f"w & s for PlayerA and 5 & 2 for PlayerB", align="center",font=("Courier",24,"normal"))

# Our main loop
while True:
    window.update()

    #Move the Ball
    ball.setx(ball.xcor() +ball.dx)
    ball.sety(ball.ycor() +ball.dy)

    # Border Checking

    if ball.ycor()>360:
        ball.sety(360)
        ball.dy*= -1

    if ball.ycor()<-360:
        ball.sety(-360)
        ball.dy*= -1

    if ball.xcor()>675:
        ball.goto(0,0)
        time.sleep(1)
        ball.dx *=-1
        score_a+=1
        pen.clear()
        pen.write(f"PlayerA: {score_a} PlayerB: {score_b}", align="center",font=("Courier",24,"normal"))


    if ball.xcor()<-675:
        ball.goto(0,0)
        time.sleep(1)
        ball.dx *=-1
        score_b+=1
        pen.clear()
        pen.write(f"PlayerA: {score_a} PlayerB: {score_b}", align="center",font=("Courier",24,"normal"))


    # Paddle and ball collision
    if ball.xcor()>600 and ball.xcor()<605 and (ball.ycor()<padd_b.ycor() + 40 and ball.ycor()>padd_b.ycor()-40):
        ball.setx(600)
        ball.dx*=-1

    if ball.xcor()<-600 and ball.xcor()>-605 and (ball.ycor()<padd_a.ycor() + 40 and ball.ycor()>padd_a.ycor()-40):
        ball.setx(-600)
        ball.dx*=-1

