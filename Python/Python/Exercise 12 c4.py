# File: <Exercise 12 c4>
# Description: <Calculating the Factorial of a Number>
# Assignment Name and Number: Chapter 4: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.
def main():
    num=int(input("Please enter a nonnegative number: "))
    print("The factorial of", num,"is",fac(num))
def fac(num):
    if num==0 or num==1:
        return 1
    else:
        return fac(num-1)*num


    fac(num)


main()