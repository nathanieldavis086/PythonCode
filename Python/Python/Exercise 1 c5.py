# File: <Exercise 1 c5>
# Description: <Kilometer Converter>
# Assignment Name and Number: Chapter 5: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.


print("This program converts a distance in kilometers into miles")
kilometers=int(input("Please enter a distance in kilometers: "))
def convert_to_miles(kilo):
    miles=kilo*0.6214
    print("There are",miles,"miles in",kilometers,"kilometers.")

convert_to_miles(kilometers)


