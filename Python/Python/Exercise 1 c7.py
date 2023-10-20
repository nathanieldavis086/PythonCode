# File: <Exercise 1 c7>
# Description: <Valid Number Information>
# Assignment Name and Number: Chapter 7: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.

valid_numbers=[]
numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

for count in range(0,10):
    num=numbers[count]
    if 0<=num<=100:
        valid_numbers.append(num)

print(valid_numbers)

sum=0
for total in valid_numbers:
    sum+=total

print("The sum of the elements of the list is", sum)
avg=sum/len(valid_numbers)
print("The average of the elements in the list is", avg)




