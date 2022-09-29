#Grphppers
import turtle as t
t.setup(700,700)
t.title('@Graphpaper Design')
h=t.Turtle()
v=t.Turtle()
h.speed(0)
v.speed(0)
h.color('coral')
v.color('coral')
for i in range(-300,301,5):
    h.setx(i);v.sety(i)
    h.pendown();v.pendown()
    h.goto(i,300);v.goto(300,i)
    h.penup();v.penup()
    h.goto(i,-300);v.goto(-300,i)
    h.pendown();v.pendown()
    h.goto(i,0);v.goto(0,i)
    h.penup();v.penup()
h.color('crimson')
v.color('crimson')    
for i in range(-300,301,50):
    h.setx(i);v.sety(i)
    h.pendown();v.pendown()
    h.goto(i,300);v.goto(300,i)
    h.penup();v.penup()
    h.goto(i,-300);v.goto(-300,i)
    h.pendown();v.pendown()
    h.goto(i,0);v.goto(0,i)
    h.penup();v.penup()
h.hideturtle()
v.hideturtle()


