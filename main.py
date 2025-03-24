import turtle
import random

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(0,200)
t.pendown()
t.pencolor('white')
t.write(("Background Color"),font=("Arial",30,"bold"),align="center")

t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor('Tan')
t.write(("1. Tan"),font=("Arial",20,"bold italic"),align="left")

t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor('Azure')
t.write(("2. Azure"),font=("Arial",20,"bold italic"),align="left")

t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor('Aquamarine')
t.write(("3. Aquamarine"),font=("Arial",20,"bold italic"),align="left")

t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor('DarkKhaki')
t.write(("4. DarkKhaki"),font=("Arial",20,"bold italic"),align="left")

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor('white')
t.write(("Choose a Color"),font=("Arial",30,"bold"),align="center")

choice = int(input("Choose a color"))

if choice == 1:
    screen.bgcolor("Tan")

elif choice == 2:
    screen.bgcolor("Azure")

elif choice == 3:
    screen.bgcolor("Aquamarine")

else:
    screen.bgcolor("DarkKhaki")

t.clear()

operation = random.randint(1,4)
if operation == 1:
    symbol = "+"
    #add
    #num1 = int(input("Enter a number: "))
    #num2 = int(input("Enter another number: "))
    num1 = random.randint(-100,100)
    num2 = random.randint(-100,100)
    solution = num1 + num2
elif operation == 2:
    symbol = "-"
    #subtraction
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)
    solution = num1 - num2
elif operation == 3:
    symbol = "*"
    #multiplication
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)

    solution = num1 * num2
elif operation == 4:
    symbol = "/"
    #division
    num1 = random.randint(-10, 10)
    num2 = random.randint(1, 100)
    sign = random.randint(1, 2)
    if sign == 2:
        num2 = -1 * num2
    solution = num1 / num2

name = input("Enter your name: ")
#num1 = int(input("Enter a number: "))
#num2 = int(input("Enter another number: "))
# num1 = random.randint(-100,100)
# num2 = random.randint(-100,100)
t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor('red')
t.write(num1,font=("Arial",25,"bold italic"),align="center")
t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor('blue')
t.write(symbol,font=("Arial",25,"bold italic"),align="center")
t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('red')
t.write(num2,font=("Arial",25,"bold italic"),align="center")
print(num1)
print(num2)
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor('green')
t.write(name,font=("Arial",25,"bold italic"),align="center")
t.penup()
t.goto(100,0)
t.pendown()
t.pencolor('blue')
t.write("=",font=("Arial",25,"bold italic"),align="center")
sum = num1 + num2
answer = float(input("What is the answer: "))
t.penup()
t.goto(200,0)
t.pendown()
t.pencolor('purple')
t.write(solution,font=("Arial",25,"bold italic"),align="center")

t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor('pink')
t.write("Your answer: "+str(answer),font=("Arial",25,"bold italic"),align="center")

if answer == solution:
    screen.bgcolor("dodgerblue")
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.pencolor('pink')
    t.write("Good Job!", font=("Arial", 25, "bold italic"), align="center")
else:
    screen.bgcolor("darkorange")
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.pencolor('magenta')
    t.write("Wrong!", font=("Arial", 25, "bold italic"), align="center")



t.hideturtle()
turtle.done()