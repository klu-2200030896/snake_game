import turtle
import time
import random

delay=0.1
#SCore
score=0
high_score=0


# set the scren
wn =turtle.Screen()
wn.title("THE NAGINI GAME 🐍🐍🐍🐍🐍🐍🐍🐍🐍")
wn.bgcolor('blue')
wn.setup(height=600,width=600)
wn.tracer(0) # turns off screen
#Snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction ="stop"
#Snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

## Segments
segments=[]

#Board
board=turtle.Turtle()
board.speed(0)
board.shape("square")
board.color("white")
board.penup()
board.hideturtle()
board.goto(0,260)
board.write("Score: 0   High Score:0",align="center",font=(" Courier ",24," normal"))




## Funtions ##
def go_up():
    if head.direction !="down":
      head.direction="up"

def go_down():
 if head.direction !="up":
    head.direction="down"

def go_left():
 if head.direction !="right":
    head.direction="left"

def go_right():
 if head.direction !="left":    
    head.direction="right"




def mov():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)


##Key Binding 
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")
#main game loop 
while True:
    wn.update()

    #check for a collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        
        # reset score
        score=0
        delay=0.1   
        board.clear()
        board.write("Score: {}   High Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))

# Check for the collinsion
    if head.distance(food)<20:
        # MOVE the food
        x= random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        # shorten the delay
        delay -=0.001

        # increase score
        score+=10
        if score>high_score:
            high_score=  score

        # update scoreboard
        board.clear()
        board.write("Score: {}   High Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))

        # MOVE the end segment
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    # MOVE the seg 0
    if len(segments)>0:
        x=head.xcor() 
        y=  head.ycor()
        segments[0].goto(x,y) 

    mov()

    # check for head collisions with body segment
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
        
            # reset score
            score=0
            delay=0.1
            board.clear()
            board.write("Score: {}   High Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))

    time.sleep(delay)
