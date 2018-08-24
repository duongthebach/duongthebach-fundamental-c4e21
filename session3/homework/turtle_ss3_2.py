from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
color("red")
for i in range(len(colors)):
    color(colors[i])
    begin_fill()
    for j in range(2): 
        forward(50)
        right(90)   
        forward(100)
        right(90)
    end_fill()
    penup()
    forward(50)
    pendown()

mainloop()