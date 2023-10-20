# File: <Exercise 7 c4>
# Description: <Pennies for Pay>
# Assignment Name and Number: Chapter 4: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.
def main():
    days=int(input("Please enter the number of days you accumulated pennies for: "))
    pay(days)

def pay(days):
    i = 1
    while days <= 0:
        days=int(input("Uh-Oh! Please enter the number of days you accumulated pennies for: "))
    while days > 0:
        
        print("By day",i,"you earned $", 0.01*(2**(i-1)))
        days = days-1
        i = i+1
    
main()