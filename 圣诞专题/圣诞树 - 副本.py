from turtle import *
#导入
import tkinter as tk
from PIL import Image, ImageTk
from time import time, sleep
from random import choice, uniform, randint
from particle import Particle

n = 70

bgpic('圣诞.gif')
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
goto(-180,100)
pendown()
ballon('green','orange')


penup()
goto(200,-120)
pendown()
ballon('red','blue')

penup()
goto(100,-150)
pendown()
ballon('red','orange')

#放烟花
# 颜色选项
colors = ['red', 'blue', 'yellow', 'white', 'green', 'orange', 'purple', 'seagreen', 'indigo', 'cornflowerblue']
HEIGHT = 800
WIDTH = 1200


def simulate(cv):
    """
        循环调用保持不停
    """
    t = time()
    explode_points = []
    wait_time = randint(10, 100)
    numb_explode = randint(5, 50)
    # 创建一个所有粒子同时扩大的二维列表
    for point in range(numb_explode):
        objects = []
        x_cordi = randint(0.05 * WIDTH, 0.95 * WIDTH)
        y_cordi = randint(0.05 * HEIGHT, 0.95 * HEIGHT)
        speed = uniform(0.2, 2.)
        size = uniform(0.2, 3)
        color = choice(colors)
        explosion_speed = uniform(0.1, 0.5)
        explosion_radius = randint(5, 15)
        total_particles = randint(20, 50)
        for i in range(1, total_particles):
            r = Particle(cv, idx=i, total=total_particles, explosion_speed=explosion_speed, explosion_radius=explosion_radius,
                         x=x_cordi, y=y_cordi, vx=speed, vy=speed, color=color, size=size, lifespan=abs(uniform(0.2, 1.75)))
            objects.append(r)
        explode_points.append(objects)

    total_time = .0
    # 1.8s内一直扩大
    while total_time < 1.8:
        sleep(0.01)
        tnew = time()
        t, dt = tnew, tnew - t
        for point in explode_points:
            for item in point:
                item.update(dt)
        cv.update()
        total_time += dt
    # 循环调用
    root.after(wait_time, simulate, cv)


def close(*ignore):
    """退出程序、关闭窗口"""
    global root
    root.quit()


if __name__ == '__main__':
    root = tk.Tk()
    cv = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    # 选一个好看的背景会让效果更惊艳！
    image = Image.open("./圣诞2.gif")
    photo = ImageTk.PhotoImage(image)

    cv.create_image(0, 0, image=photo, anchor='center')
    cv.pack()

    root.protocol("WM_DELETE_WINDOW", close)
    root.after(100, simulate, cv)
    root.mainloop()
