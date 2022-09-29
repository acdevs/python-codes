#fibonacchi spiral
import turtle as t
t.setup(1000,1000)
t=t.Turtle()
t.speed(10)
t.pensize(2)
f=-1
s=1
for i in range(10):
    p=f+s
    f,s=s,p
    t.circle(p*5,180)
    

