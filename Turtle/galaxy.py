#fibonacchi spiral
import turtle as t
t.setup(1000,1000)
t1=t.Turtle()
t2=t.Turtle()
t3=t.Turtle()
t4=t.Turtle()
t1.speed(100);t2.speed(100);t3.speed(100);t4.speed(100);
f=-1
s=1
t1.lt(0)
t2.lt(90)
t3.lt(180)
t4.lt(270)
for i in range(15):
    p=f+s
    f,s=s,p
    t1.circle(p,90)
    t2.circle(p,90)
    t3.circle(p,90)
    t4.circle(p,90)


