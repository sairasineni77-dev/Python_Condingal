import turtle
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.title("Turtle")
my_pen = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        my_pen.fd(size + 1)
        my_pen.left(90)
        print("The value of size before updation", size)
        size = size - 5
        print("The value of size after updation", size)
    size = size + 1
    print("The final size", size)