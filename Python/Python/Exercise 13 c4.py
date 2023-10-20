# File: <Exercise 13 c4>
# Description: <Population>
# Assignment Name and Number: Chapter 4: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.
initial=int(input("Please enter the starting population: "))
average_increase=int(input("Please enter the average percent daily increase: "))/100
num_days=int(input("Please enter the number of days the population was allowed to grow: "))
i = 0
pop=initial

while initial<=0 or average_increase<=0 or num_days<=0:
    print("Please enter positive numbers only")
    initial=int(input("Please enter the starting population: "))
    average_increase=int(input("Please enter the average percent daily increase: "))/100
    num_days=int(input("Please enter the number of days the population was allowed to grow: "))

print("On day",i,"your population was",pop)

while initial>0 and average_increase>0 and num_days>0:
        i += 1
        pop=pop + pop*(average_increase)
        print("On day",i,"your population was",pop)
        num_days=num_days-1
        
        
print("Your final population will be",pop)