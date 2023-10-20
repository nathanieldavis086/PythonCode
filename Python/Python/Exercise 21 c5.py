# File: <Exercise 13 c5>
# Description: <Rock Paper Scissors>
# Assignment Name and Number: Chapter 5: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.

import random
#1=rock
#2=paper
#3=scissors
print("Let's play rock paper scissors")
def rps():
    computer_num=random.randint(1,3)
    user_input=input("Please enter rock, paper, or scissors: ")


    if user_input=="rock":
        user_num=1
    elif user_input=="paper":
        user_num=2
    elif user_input=="scissors":
        user_num=3
    else:
        print("Please enter rock, paper, or scissors with no capital letters")
        rps()
    

    if computer_num==1:
        print("I picked rock.")
    elif computer_num==2:
        print("I picked paper.")
    elif computer_num==3:
        print("I picked scissors.")


    if user_num==computer_num:
        print("We tied. Let's play again.")
        rps()
    elif computer_num==1 and user_num==2:
        print("You win.")
    elif computer_num==1 and user_num==3:
        print("I win.")
    elif computer_num==2 and user_num==1:
        print("I win.")
    elif computer_num==2 and user_num==3:
        print("You win.")
    elif computer_num==3 and user_num==1:
        print("You win.")
    elif computer_num==3 and user_num==2:
        print("I win.")

rps()
