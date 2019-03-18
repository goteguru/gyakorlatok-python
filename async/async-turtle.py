import turtle 
import time

def box(t, n):
    turtle.begin_fill()
    for _ in range(4):
        t.forward(n)
        t.right(90)
    turtle.end_fill()


if __name__ == "__main__":
    turtle.speed(0)
    turtle.tracer(0)
    turtle.hideturtle()
    s = turtle.getscreen()

    bob = turtle.Turtle()
    krisz = turtle.Turtle()

    while True: 
        bob.clear()
        box(bob,30)
        bob.left(2)
        bob.forward(4)
        
        krisz.clear()
        box(krisz,40)
        krisz.left(1)
        krisz.forward(2)
        s.update()
        time.sleep(0.01)
        
    s.exitonclick()
