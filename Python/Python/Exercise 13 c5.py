
# File: <Exercise 13 c5>
# Description: <Falling Distance>
# Assignment Name and Number: Chapter 5: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.

print("This program will tell you how far an object has fallen based on how long it has been falling for")
g=9.8

def falldist(t):
    d=0.5*g*t**2
    return d
for t in range (10):
    d=falldist(t)

    print(d)