from turtle import *

t = Turtle()
t.color('black')
t.penup()
t.goto(-233, -170)
t.pendown()
t.left(90)
t.forward(450)
t.right(90)
t.forward(450)
t.right(90)
t.forward(450)
t.right(90)
t.forward(450)
t.right(180)
t.hideturtle()

t2 = Turtle()
t2.penup()
t2.goto(-200, 200)
t2.pendown()
t2.color('black')
t2.write("0", font = ('Arial', 50, 'normal'))
t2.hideturtle()

class Sprite(Turtle):
    def __init__(self, x, y, step=10, shape='circle', color='black'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)

    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)

    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 30:
            return True 
        else:
            return False

    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))

    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)

player = Sprite(0, -100, 10, 'circle', 'orange')
enemy1 = Sprite(-200, 0, 25, 'square', 'red')
enemy1.set_move(-200, 0, 200, 0)
enemy2 = Sprite(200, 50, 25, 'square', 'red')
enemy2.set_move(200, 50, -200, 50)
enemy3 = Sprite(-200, 100, 25, 'circle', 'red')
enemy3.set_move(-200, 100, 200, 100)
enemy4 = Sprite(200, -50, 25, 'circle', 'red')
enemy4.set_move(200, -50, -200, -50)
finish = Sprite(0,200, 10, 'triangle', 'green')

scr = player.getscreen()
scr.listen()
scr.onkey(player.move_up, 'w')
scr.onkey(player.move_left, 'a')
scr.onkey(player.move_right, 'd')
scr.onkey(player.move_down, 's')

total_score = 0
while total_score < 3:
    enemy1.make_step()
    enemy2.make_step()
    enemy3.make_step()
    enemy4.make_step()
    if player.is_collide(finish):
        player.goto(0, -100)
        total_score += 1
        t2.clear()
        t2.write(total_score, font = ('Arial', 50, 'normal'))
    if abs(player.xcor()) > 233 or abs(player.ycor()) > 170:
        player.penup()
        player.goto(0, -100)
    if player.is_collide(enemy1) or player.is_collide(enemy2) or player.is_collide(enemy3) or player.is_collide(enemy4):
        finish.hideturtle()
        break
enemy1.hideturtle()
enemy2.hideturtle()
enemy3.hideturtle()
enemy4.hideturtle()
if total_score >= 3:
    t2.penup()
    t2.goto(-150, 0)
    t2.pendown()
    t2.color('green')
    t2.clear()
    t2.write('YOU WIN!', font = ('Arial', 25, 'normal'))
else:
    t2.penup()
    t2.goto(-150, 0)
    t2.pendown()
    t2.color('red')
    t2.clear()
    t2.write('YOU LOSE!', font = ('Arial', 25, 'normal'))
