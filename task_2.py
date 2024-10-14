import turtle
import sys


def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)
        t.right(120)
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)


def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)


def main():
    if len(sys.argv) != 2:
        print("Usage: python task_2.py <recursion_level>")
        sys.exit(1)

    level = int(sys.argv[1])

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    koch_snowflake(t, 400, level)

    turtle.done()


if __name__ == "__main__":
    main()
