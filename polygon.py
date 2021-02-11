import turtle
Bob=turtle.Turtle()


def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def triangle(t, n, length):
    for i in range(3):
        t.lt(((n-2)*180)/2)
        t.fd(length)
        t.lt(360/n)
        t.fd

turtle.mainloop()