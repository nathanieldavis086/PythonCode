# File: <Exercise 6 c7>
# Description: <Dice Rolling Function>
# Assignment Name and Number: Chapter 7: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.

import random
roll_results=[]
def roll(number_of_throws):
    for count in range(number_of_throws):
        result=random.randint(1,6)
        roll_results.append(result)
    roll_results.sort()
    return print("The roll results are:",roll_results)
number_of_rolls=int(input("Please enter a number of times to roll: "))
roll(number_of_rolls)





