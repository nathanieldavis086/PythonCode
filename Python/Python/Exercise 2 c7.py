# File: <Exercise 2 c7>
# Description: <Lottery Number Generator>
# Assignment Name and Number: Chapter 7: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.


import random
list=[]
index=0


for count in range(0,7):
    number=random.randint(0,10)
    list.append(number)
    index+=1
print(list)
    