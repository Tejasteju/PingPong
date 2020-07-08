import turtle
import time
import sys


win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)

#Score
game_point = 3 # Sets the Game_Point
Game_speed= 0.2 # Sets the Game_speed
score_a = 0
score_b = 0


def reset_score():
    return 0

#Left Paddle
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.color("blue")
paddle_l.shapesize(stretch_wid=3, stretch_len=0.7)
paddle_l.penup()
paddle_l.goto(-375,0)


#Right Paddle
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color("red")
paddle_r.shapesize(stretch_wid=3, stretch_len=0.7)
paddle_r.penup()
paddle_r.goto(375,0)

#Ball
pong = turtle.Turtle()
pong.speed(0)
pong.shape("circle")
pong.color("white")
pong.shapesize(stretch_wid=0.3, stretch_len=0.3)
pong.penup()
pong.goto(0,0)
pong.dx = Game_speed
pong.dy = Game_speed

#Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("grey")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0", align='center', font=('Arial',24,'normal'))


#Funtion
def paddle_l_up():
    if(paddle_l.ycor()!=300):
        y = paddle_l.ycor()
        y += 20
        paddle_l.sety(y)

def paddle_l_down():
    if(paddle_l.ycor()!=-300):
        y = paddle_l.ycor()
        y -= 20
        paddle_l.sety(y)

def paddle_r_up():
    if(paddle_r.ycor()!=300):
        y = paddle_r.ycor()
        y += 20
        paddle_r.sety(y)

def paddle_r_down():
    if(paddle_r.ycor()!=-300):
        y = paddle_r.ycor()
        y -= 20
        paddle_r.sety(y)

#Key Binding
win.listen()
win.onkeypress(paddle_l_up,"w")
win.onkeypress(paddle_l_down,"s")
win.onkeypress(paddle_r_up,"Up")
win.onkeypress(paddle_r_down,"Down")
#win.onkeypress(sys.exit(),"Q")


#main loop
while True:
    win.update()
    if(score_a == game_point):
        pen.clear()
        pen.write("PLAYER A WON",align ="center",font=('Arial',24,'normal'))
        time.sleep(2)
        pen.clear()
        pen.write("Player A: 0   Player B: 0", align='center', font=('Arial',24,'normal'))
        score_a = reset_score()
        score_b = reset_score()
    
    elif(score_b == game_point):
        pen.clear()
        pen.write("PLAYER B WON",align ="center",font=('Arial',24,'normal'))
        time.sleep(2)
        pen.clear()
        pen.write("Player A: 0   Player B: 0", align='center', font=('Arial',24,'normal'))
        score_a = reset_score()
        score_b = reset_score()
    
    #Move the Pong
    pong.setx(pong.xcor() + pong.dx)
    pong.sety(pong.ycor() + pong.dy)

    #Border checking
    if pong.ycor()>290:
        pong.sety(290)
        pong.dy *= -1

    if pong.ycor()<-290:
        pong.sety(-290)
        pong.dy *= -1

    if pong.xcor()>390:
        time.sleep(0.7)
        pong.goto(0,0)
        pong.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b) , align='center', font=('Arial',24,'normal'))
    
    if pong.xcor()<-390:
        time.sleep(0.7)
        pong.goto(0,0)
        pong.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b) , align='center', font=('Arial',24,'normal')) 

    #Collision
    if pong.xcor() > 370 and pong.xcor() < 375 and (pong.ycor() < paddle_r.ycor() + 40 and pong.ycor() > paddle_r.ycor() - 40):
        pong.setx(370)
        pong.dx *= -1

    if pong.xcor() < -370 and pong.xcor() > -375 and (pong.ycor() < paddle_l.ycor() + 40 and pong.ycor() > paddle_l.ycor() - 40):
        pong.setx(-370)
        pong.dx *= -1