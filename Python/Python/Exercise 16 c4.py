# File: <Exercise 13 c4>
# Description: <Squares*100>
# Assignment Name and Number: Chapter 4: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.

import turtle
separate=0
i=0
turtle.width(2)
reps=100
turtle.speed(9)
for squares in range (reps):
    turtle.left(90)
    turtle.forward(10+i+separate)
    turtle.left(90)
    turtle.forward(10+i+separate)
    turtle.left(90)
    turtle.forward(10+i+separate)
    turtle.left(90)
    turtle.forward(10+i+separate)
    separate+=5
    i+=10