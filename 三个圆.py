import turtle
t = turtle


#设置区，用于设置全局变量
speed = 10 #全局绘图速度
m = 8 #三角形边长
n = 3 #想画几个气球
r = 20 #每个气球圆的半径
x = 40 #每个气球间横坐标偏移
y = 60 #每个气球间纵坐标偏移



#定义几个函数（多个气球的话纯循环不好实现）
def line():
    t.begin_fill()
    for i in range(3):
        t.forward(m)
        t.left(120)
    t.end_fill()
    t.setheading(0)
    t.forward(m/2)
    t.setheading(270)
    t.forward(70)
    t.setheading(0) #这个朝向一定要想清楚

def reset():
    t.reset
    t.speed(speed)
    t.bgpic('海底.gif')

def cir():
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def ballon(p1,f1):
    t.pencolor(p1)
    t.fillcolor(f1)
    cir()
    t.right(120)
    t.forward(m)
    t.setheading(0)
    line()

#执行
reset()

ballon('blue','red')
t.penup()
t.goto(100,-100)
t.pendown()

ballon('white','blue')
t.penup()
t.goto(200,-200)
t.pendown()

ballon('gold','grey')
t.penup()
t.goto(300,-300)
t.pendown()

t.done()