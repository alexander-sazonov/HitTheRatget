import turtle as t
import random
WIDTH = 800
HEIGHT = 600
TARGET_SIZE = 100
t.setup(WIDTH, HEIGHT)
t.bgcolor('lightblue')
x_target = random.randint(- WIDTH / 2 + TARGET_SIZE, WIDTH / 2 - TARGET_SIZE)
y_target = random.randint(- HEIGHT / 2 + TARGET_SIZE, HEIGHT / 2 - TARGET_SIZE)
t.penup()
t.goto(x_target, y_target)
t.pendown()
t.forward(TARGET_SIZE)
t.left(90)
t.forward(TARGET_SIZE)
t.left(90)
t.forward(TARGET_SIZE)
t.left(90)
t.forward(TARGET_SIZE)
t.left(90)
t.mainloop()