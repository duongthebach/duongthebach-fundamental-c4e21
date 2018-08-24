from turtle import *

Turtle()

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(len(colors)):
    color(colors[i])
    a = i +3
    for j in range(a):
        forward(100)
        left(360/a)
mainloop()
