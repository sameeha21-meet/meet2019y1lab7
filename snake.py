import turtle
import random
turtle.tracer(1,0)
size_x=800
size_y=500
turtle.setup(size_x,size_y)
turtle.penup()
square_size=20
start_length=6
time_step=100
#initialize lists
pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]
snake=turtle.clone()
snake.shape("square")
turtle.hideturtle()
def new_stamp():
    snake_pos=snake.pos()
    pos_list.append(snake_pos)
    snakeID=snake.stamp()
    pos_list.append(snakeID)
for i in range (start_length):
   x_pos=snake.pos()[0]
   y_pos=snake.pos()[1]
   x_pos+=square_size
   snake.goto(x_pos,y_pos)
   new_stamp()
turtle.mainloop()
def remove_tail():
    old_stamp=stamp_list.pop
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
snake.direction="up"
def up:()
    snake.direction="up"
    move_snake()
    print("you pressed the up key!")
def down():
     snake.direction="down"
    move_snake()
    print("you pressed the up key!")
def left():
     snake.direction="left"
    move_snake()
    print("you pressed the up key!")
def right():
     snake.direction="right"
    move_snake()
    print("you pressed the up key!")
turtle.onkeypress(up,"up")
turtle.onkeypress(down,"down")
turtle.onkeypress(left,"left")
turtle.onkeypress(left,"left")
turtle.listen()
def move_snake():
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
if snake.direction=="up":
    snake.goto(x_pos,y_pos+square_size)
    print("you moved up!")
elif snake.direction=="down"():
    snake.goto(x_pos,y_pos+square_size)
    print("you moved down!")
elif snake.dire
    
