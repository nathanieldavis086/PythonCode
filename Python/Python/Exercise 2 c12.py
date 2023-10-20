# File: <Exercise 2 c12>
# Description: <Recursive Multiplication>
# Assignment Name and Number: Chapter 7: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.

num1=int(input("Please enter a number: "))
num2=int(input("Please enter another number: "))

def add(x,y):
    if x==0 or y==0:
        return print("0")
    else:
        for count in range (y):
            mult=x+add(x,y-1)
            return print(mult)
add(num1,num2)















#def main():


 #   def add(x,y):
       # x=int(input("Please enter a number: "))
       # y=int(input("Please enter another number: "))

       # if x==0 or y==0:
      #      return 0
      #  elif x<0 or y<0:
      #      print("Please enter valid numbers")
      #  else:
      #      y-=1
       #     answer=x+add(x,y)
        #    print("The product of",x,"and",y,"is", answer)
#main()