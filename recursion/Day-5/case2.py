# 可视化递归算法

# import turtle

# # myTurtle = turtle.Turtle()  # 🐢对象（初始状态）
# # myScreen = turtle.Screen()  #  绘制窗口

# 递归绘制螺旋
# # def drawSpiral(myTurtle,lineLen):
# #     if lineLen > 0:
# #         myTurtle.forward(lineLen)
# #         myTurtle.right(90)
# #         drawSpiral(myTurtle,lineLen - 5)

# # drawSpiral(myTurtle,100)
# # myScreen.exitonclick() 

# 树
# def tree(branchLen,t):
#     if branchLen > 5:
#         t.forward(branchLen)
#         t.right(45)
#         tree(branchLen-15,t)
#         t.left(90)
#         tree(branchLen-15,t)
#         t.right(45)
#         t.backward(branchLen)

# def main():
#     t = turtle.Turtle()
#     myScreen = turtle.Screen()

#     t.left(90)
#     t.up()
#     t.backward(100)
#     t.down()
#     t.color("red")
#     tree(75,t)
#     myScreen.exitonclick()

# main()


# 太阳花
# import turtle
# import time
# # 同时设置pencolor=color1, fillcolor=color2
# turtle.color("red", "yellow")
# turtle.begin_fill()
# for _ in range(50):
#     turtle.forward(200)
#     turtle.left(170)
# turtle.end_fill()
    
# turtle.mainloop()




# 汉诺塔

# def hanoi(n,x,y,z):
#     if n == 1:
#         print(x,'->',z)
#     else:
#         hanoi(n-1,x,z,y)#将前n-1个盘子从x移动到y上
#         print(x,'-->',z)#将最底下的最后一个盘子从x移动到z上
#         hanoi (n-1,y,x,z)#将y上的n-1个盘子移动到z上

# n = int(input('请输入汉诺塔的层数：'))
# hanoi(n,'x','y','z')



# from pythonds.basic.stack import Stack

# def moveTower(height,fromPole,toPole,withPole):
#     if height >= 1:
#         moveTower(height - 1,fromPole,withPole,toPole)
#         moveDisk(fromPole,toPole)
#         moveTower(height-1,withPole,toPole,fromPole)

# def moveDisk(fp,tp):
#     print("移动盘子，从",fp,"到",tp)


# fromPole = Stack()
# toPole = Stack()
# withPole = Stack()

# moveTower(5,fromPole,toPole,withPole)
















