#Просто нажмите "run" и сами всё увидите
import time
import datetime as dt
import turtle

# создаем черепашку для отображения времени
t = turtle.Turtle()
# создаем черепашку для создания прямоугольника
t1 = turtle.Turtle()
# создать экран
s = turtle.Screen()
# Цвет экрана
s.bgcolor("white")

# получить текущий час, минуту и секунду
# из системы
sec = dt.datetime.now().second
minn = dt.datetime.now().minute
hr = dt.datetime.now().hour

t1.pensize(5)
t1.color('Green')
t1.penup()
# устанавливаем положение черепашки
t1.goto(-29, 2)
# скорость черепахи
t1.speed(4.70)
t1.pendown()

# создаем прямоугольную рамку
for i in range(2):
    t1.forward(200)
    t1.left(90)
    t1.forward(70)
    t1.left(90)

# спрятать черепаху
t1.hideturtle()

while True:
    t.hideturtle()
    t.clear()
    # отображать время
    t.write(str(hr).zfill(2)+":"+str(minn).zfill(2)+":"+str(sec).zfill(2),
            font=("Arial Narrow", 35, "bold"))
    # t.write(str(hr).zfill(2)
    #         + ":"+str(minn).zfill(2)+":"
    #         + str(sec).zfill(2),
    #         font=("Arial Narrow", 35, "bold"))
    time.sleep(1)
    sec += 1

    if sec == 60:
        sec = 0
        minn += 1

    if minn == 60:
        minn = 0
        hr += 1

    if hr == 13:
        hr = 1




















