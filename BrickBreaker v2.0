import turtle
import random

screenx = 5
screeny = 6.5



wn = turtle.Screen()
wn.title('Brick Breaker')
wn.bgcolor('black')
wn.setup(screenx, screeny)

px = 0
py = -350

bx = 0
by = -330

#player
player = turtle.Turtle()
player.penup()
player.speed(0)
player.color('white')
player.shape('square')
player.shapesize(0.5, 5.5)
player.setpos(px,py)

#ball
ball = turtle.Turtle()
ball.penup()
ball.speed(0)
ball.color('white')
ball.shape('circle')
ball.shapesize(1, 1)
ball.setpos(bx,by)

def right():
    px = player.xcor()
    px += 50
    player.setpos(px,py)

def left():
    px = player.xcor()
    px -= 50
    player.setpos(px,py)

wn.listen()
wn.onkeypress(left, 'Left')
wn.onkeypress(right, 'Right')


dscreenx = 5
dscreeny = 6.5

while True:
    screenx += dscreenx
    screeny += dscreeny
    if screenx > 600:
        dscreenx = 0

    if screeny > 800:
        dscreeny = 0

    wn.setup(screenx, screeny)
    wn.update()
