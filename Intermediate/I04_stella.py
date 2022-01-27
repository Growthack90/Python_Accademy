"""Disegna una stella a 5 punte"""
import turtle 

star = turtle.Turtle()
star.pensize(35)
star.pencolor("green4")
star.hideturtle()

for i in range(5):
    star.forward(500)
    star.right(144)
    
turtle.done()
