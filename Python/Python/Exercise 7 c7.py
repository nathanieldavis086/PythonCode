# File: <Exercise 7 c7>
# Description: <Driver's License Exam>
# Assignment Name and Number: Chapter 7: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.

correct_answers=['a','c','a','a','d','b','c','a','c','b','a','d','c','a','d','c','b','b','d','a']
user_answers=[]


answer1=input("Please enter the answer you entered for problem 1: ")
user_answers.append(answer1)

for count in range(19):
    answer=input("Please enter the answer you entered for the next problem: ")
    user_answers.append(answer)

x = 0
correct = 0
incorrect = 0

while x < len(correct_answers):
    if user_answers[x] == correct_answers[x]:
        correct+=1
        x+=1
    else:
        incorrect+=1
        x+=1

print("You got",correct,"answers right and",incorrect,"answers wrong.")
score=correct/20*100
print("You got a score of",score,"percent.")

if score>=75:
    print("You passed")
else:
    print("You failed")