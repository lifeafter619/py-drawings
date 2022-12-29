import turtle as t 
t.hideturtle()
t.bgpic('海底.gif')
t.pensize(2)
pcolor=['yellow','green','red','blue','gray']	#创建列表
fcolor=['pink','orange','purple','gold','brown']	#创建列表
t.speed(20)

for i in range(5):
   t.pencolor(pcolor[i])	#设置第 i 个气球的线色为 pcolor[i]
   t.fillcolor(fcolor[i])	#设置第 i 个气球的填充色为 fcolor[i] 
   #画圆
   t.up() 
   t.goto(0+68*i,0+10*i) 
   t.down()
   t.begin_fill() 
   t.circle(20) 
   t.end_fill()  #画三角形
   t.up()
   t.goto(-6+68*i,-10+10*i) 
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
   t.goto(0+68*i,0+10*i) 
   t.pendown() 
   t.right(90) 
   t.forward(80) 
   t.setheading(0)
t.done()