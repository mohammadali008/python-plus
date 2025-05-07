# 06-Session
# - turtle-lib for drawing shapes
import turtle as tl
tl.pencolor('black')
tl.pensize(5)
tl.speed('slow')  
tl.fillcolor('blue') 
##-- draw square
# for i in range(4):
#     tl.forward(200)
#     tl.right(90)
# #-- Draw Rectangle
for i in range(5):
    if i%2 != 0:
        tl.forward(200)
        tl.right(90)
    else:
        
        tl.forward(100)


# ##-- Draw Pentagon
# tl.penup()
# tl.goto(-200,20)
# tl.pendown()
# tl.begin_fill()
# for i in range(5):
#     tl.backward(200)
#     tl.left(72)
##-- Draw Star
##-- Draw Pentagon 
tl.penup()
tl.goto(-200,20)
tl.pendown()
tl.begin_fill()
# for i in range(5):
#     tl.backward(200)
#     tl.left(144)
##-- Draw Circle
# tl.circle(100)
##-- Get data as list from user and plot it with turtle
# data = input("Enter data :").split() #we can use turtle.input(,) instead of input() 
# for i in data:
#     tl.forward(10)
#     tl.left(90)
#     tl.forward(int(i))
#     tl.right(90)
#     tl.forward(40)
#     tl.right(90)
#     tl.forward(int(i))
#     tl.left(90)
#     tl.forward(10)
##-- 









tl.end_fill()

## It's neccecery to show turtle's window
tl.done()
