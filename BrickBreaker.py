import turtle
import winsound

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=800, height=800)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape('square')
paddle.color('white')
paddle.penup()
paddle.goto(0, -350)
paddle.shapesize(1, 5)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.goto
ball.penup()
ball.dx = 0.1
ball.dy = 0.1


def paddle_left():
    x = paddle.xcor()
    x += -20
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_left, 'a')
wn.onkeypress(paddle_right, 'd')



# Main game loop
while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor()>390:
        ball.sety(390)
        ball.dy *= -1

    if ball.xcor()>390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor()<-405:
        ball.goto(0, 0)


    if ball.distance(paddle)<50:
        ball.sety(-300)
        ball.dy*= -1
