# File: <Exercise 13 c7>
# Description: <Magic 8 Ball>
# Assignment Name and Number: Chapter 7: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.

import random

answers=["Yes, of course!","Without a doubt, yes","You can count on it","For sure","Ask me later","I'm not sure","I can't tell you right now","I'll tell you after my nap","No way!","I don't think so","Without a doubt, no","The answer is clearly NO"]


def eightball():
    input("Ask me a question, any question: ")
    answer=answers[random.randint(0,12)]
    print(answer)
    again=input("Play again? Enter 'yes' or 'no': ")
    if again=="yes":
        eightball()
    if again=="no":
        return
eightball()




    
