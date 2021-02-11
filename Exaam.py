import turtle
import math
t=turtle.Turtle()
bob=turtle.Turtle()

def square(t, length):
    
    for i in range(4):
        t.fd(length)
        t.lt(90)

def passer(y, x):
    y(x)


    
def polygon(t, length, n):
    #draws a polygon with number of sides n and length of sides length
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

#polygon(bob, 100, 7)


def circle(t, r):
   c= 2*math.pi*r
   n=int(c/3)+1
   length=c/n
   polygon(t, length, n)

def polyline(t, length, n, angle):
    
    for i in range(n):
        t.fd(length)
        t.lt(angle/n)
    


def arc(t, r, angle):
   s= 2*math.pi*r*(angle/360)
   n=int(s/3)+1
   length=s/n
   polyline(t, length, n, angle)





   



def flower2(t, r, n):
    for i in range(n):
        arc(t, r, (float(720/5)))
        t.lt(float(108))
    



def petal(t, r, angle):
    for i in range(2):
        arc(t, r, (angle))
        t.lt(float(180-angle))

def flower1(t, r, n, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)
                     
flower1(bob, 90, 7, 60)

bob.pu()
bob.fd(120)
bob.pd()

flower1(bob, 140, 20, 20)

turtle.mainloop()

   


   
