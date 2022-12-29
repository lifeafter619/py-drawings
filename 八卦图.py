from turtle import *
def yin(radius, color1, color2):
    width(3)		# 设置画笔的宽度
    color("black", color1)  	# 设置画笔颜色
    begin_fill()		# 执行填充
    circle(radius/2., 180)  	# 绘制半径为radius/2，弧度为180度的线
    circle(radius, 180)
    left(180) 		# 向左转动180度
    circle(-radius/2., 180)  
    end_fill()
    left(90)
    up()
    forward(radius*0.35)  # 向前移动radius*0.35像素，移动距离根据原图计算得出
    right(90)
    down()
    color(color1, color2)
    begin_fill()
    circle(radius*0.15)
    end_fill()	# 结束填充
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)
def main():
    reset()  	# 重置turtle
    yin(200, "black", "white")
    yin(200, "white", "black")
    ht()  	# 隐藏turtle

main()
done()