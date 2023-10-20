# File: <Exercise 7 c5>
# Description: <Satdium Seating>
# Assignment Name and Number: Chapter 5: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.

aseats=int(input("Please enter how many A class seats you sold: "))
bseats=int(input("Please enter how many B class seats you sold: "))
cseats=int(input("Please enter how many C class seats you sold: "))

def a(seats):
    income=seats*20
    return income

def b(seats):
    income=seats*15
    return income

def c(seats):
    income=seats*10
    return income

total_income=a(aseats)+b(bseats)+c(cseats)

print("The total income was",total_income)