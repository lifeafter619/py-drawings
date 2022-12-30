from turtle import *

n = 70

speed("fastest")
pensize(2.5)
left(90)
forward(200)
color("orange", "yellow")
begin_fill()
left(126)

for i in range(5):
    forward(n/5)
    right(144)
    forward(n/5)
    left(72)
end_fill()
right(126)

color("green")
backward(n * 3.8)


def tree(d, s):
    if d <= 0: return
    forward(s)
    tree(d-2, s*0.8)
    right(120)
    tree(d-3.3, s*0.75)
    right(120)
    tree(d-3.3, s*0.75)
    right(120)
    backward(s)


tree(12, n)
backward(n+10)

#设置区，用于设置全局变量
m = 8 #三角形边长
n = 2 #想画几个气球
r = 20 #每个气球圆的半径
x = 40 #每个气球间横坐标偏移
y = 60 #每个气球间纵坐标偏移



#定义几个函数（多个气球的话纯循环不好实现）
def line():
    begin_fill()
    for i in range(3):
        forward(m)
        left(120)
    end_fill()
    setheading(0)
    forward(m/2)
    setheading(270)
    forward(70)
    setheading(0) #这个朝向一定要想清楚

def reset():
    penup()
    goto(0,0)
    setheading(0)
    bgpic('圣诞.jpg')
    pendown()

def cir():
    begin_fill()
    circle(r)
    end_fill()

def ballon(p1,f1):
    pencolor(p1)
    fillcolor(f1)
    cir()
    right(120)
    forward(m)
    setheading(0)
    line()

#执行
reset()

penup()
goto(-300,150)
pendown()
ballon('green','orange')


penup()
goto(300,-150)
pendown()
ballon('red','blue')

penup()
goto(100,-150)
pendown()
ballon('red','orange')


done()
