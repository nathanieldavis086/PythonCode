# File: <Exercise 4 c7>
# Description: <Number Analysis Program>
# Assignment Name and Number: Chapter 7: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.

numbers=[]

for count in range(0,20):
    numbers.append(int(input("Please enter a number: ")))

max=max(numbers)
min=min(numbers)
print(max,"is the highest number in the list")
print(min,"is the lowest number in the list")

sum=0
for acc in numbers:
    sum+=acc
print("The sum of all the numbers is",sum)

avg=sum/len(numbers)
print("The average of the numbers is",avg)
