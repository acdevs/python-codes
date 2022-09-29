#fibonacchi spiral
import turtle as t
t.setup(1000,1000)
t.lt(0)
f=-1
s=1
for i in range(15):
    p=f+s
    f,s=s,p
    t.circle(p,90)

