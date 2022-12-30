import turtle as t 
import time
t.hideturtle()		#不显示画笔
t.tracer(0)	#不显示绘画过程
t.bgpic('海底.gif') 
t.pensize(2)
t.pencolor('yellow') 
t.fillcolor('yellow') 
t.speed(20)
while(1):	#一直循环
    for i in range(40):
        #画圆
        t.up()
        t.goto(0+18*i,0+10*i)	#每次循环，圆水平方向移动 18，竖直方向移动 10 
        t.down()
        t.begin_fill() 
        t.circle(40) 
        t.end_fill()  #画三角形
        t.up()
        t.goto(-6+18*i,-10+10*i) #每次循环，三角形水平方向移动 18，竖直方向移动 10 
        t.down()
        t.begin_fill() 
        t.forward(12) 
        t.left(120) 
        t.forward(12) 
        t.left(120) 
        t.forward(12) 
        t.left(120) 
        t.end_fill()
        #画直线
        t.penup()
        t.goto(0+18*i,0+10*i)	#每次循环，直线水平方向移动 18，竖直方向移动 10 
        t.pendown()
        t.right(90) 
        t.forward(80) 
        t.setheading(0)
        t.update()	#更新画布内容
        t.clear()	#清除画布内容
        time.sleep(1/10)	#程序等待 1/10 秒