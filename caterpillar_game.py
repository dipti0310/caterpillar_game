import turtle as t
import random as rd
t.bgcolor('yellow')
caterpillar=t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

leaf=t.Turtle()
leaf_shape=((0,0),(14,2),(18,6),(20,20),(2,14),(6,18))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.fillcolor('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()

start_game=False
text_start=t.Turtle()
text_start.write("Press SPACE to start",align='center',font=('Arial',18,'bold'))
text_start.hideturtle()

display_score=t.Turtle()
display_score.hideturtle()
display_score.speed(0)

def out_window():
    left_width=(-t.window_width()/2)
    right_width=(t.window_width()/2)
    top_width=(t.window_height()/2)
    bottom_width=(-t.window_height()/2)
    (x,y)=caterpillar.pos()
    coll=x< left_width or x >right_width or y< bottom_width or y>top_width
    return coll
def game_over():
        caterpillar.color('yellow')
        leaf.color('yellow')
        t.penup()
        t.hideturtle()
        t.write("GAME OVER!",align='center',font=('Arial',18,'bold'))

def show_score(current_score):
    display_score.clear()
    display_score.penup()
    x=(t.window_width()/2)-50
    y=(t.window_height()/2)-50
    display_score.setpos(x,y)
    display_score.write(str(current_score),align='right',font=('Arial',18,'bold'))
def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

def main():
    global start_game
    if start_game:
        return
    start_game=True
    score=0
    text_start.clear()
    caterpillar_speed=4
    caterpillar_length=3
    caterpillar.shapesize(1,caterpillar_length,1)
    caterpillar.showturtle()
    show_score(score)
    place_leaf()
    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf)<20:
            place_leaf()
            caterpillar_length=caterpillar_length+1
            caterpillar.shapesize(1,caterpillar_length,1)
            caterpillar_speed=caterpillar_speed+1
            score=score+10
            show_score(score)
        if out_window():
            game_over()
            break
def move_up():
    if caterpillar.heading()==0 or caterpillar.heading()==180:
        caterpillar.setheading(90)
def move_down():
    if caterpillar.heading()==0 or caterpillar.heading()==180:
        caterpillar.setheading(270)
def move_right():
    if caterpillar.heading()==90 or caterpillar.heading()==270:
        caterpillar.setheading(0)
def move_left():
    if caterpillar.heading()==90 or caterpillar.heading()==270:
        caterpillar.setheading(180)
t.onkey(main,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()
