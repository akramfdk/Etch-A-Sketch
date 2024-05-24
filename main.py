import turtle as t

pen = t.Turtle()
window = t.Screen()


def move_forwards():
    pen.forward(10)


def move_backwards():
    pen.backward(10)


def rotate_counter_clockwise():
    pen.left(5)


def rotate_clockwise():
    pen.right(5)


def clear_screen():
    window.reset()
    # pen.clear()
    # pen.up()
    # pen.home()
    # pen.down()


window.listen()
window.onkey(fun=move_forwards, key="w")
window.onkey(fun=move_backwards, key="s")
window.onkey(fun=rotate_counter_clockwise, key="a")
window.onkey(fun=rotate_clockwise, key="d")
window.onkey(fun=clear_screen, key="c")


window.exitonclick()
