import turtle

#也许这样更好，免得debug报错
t = turtle

#设置
t.reset()
t.pendown()
t.bgpic('海底.gif')
t.pencolor('gold')
t.fillcolor('light blue')

#画圆
t.goto(0,0)
t.begin_fill()
t.circle(30)
t.end_fill()

#画三角形
n = 3 #n边形
m = 10 #n边形边长
t.setheading(0) #保证多边形在中央
t.forward(m/2)
t.setheading(180)

t.fillcolor('gold')
t.begin_fill()
for i in range(n):
   t.forward(m)
   t.left(360/n)
t.end_fill()
t.setheading(180)
t.forward(m/2)


t.setheading(270)
t.forward(70)
t.penup() #准备下一次绘制
t.done()