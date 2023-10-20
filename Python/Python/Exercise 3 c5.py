# File: <Exercise 3 c7>
# Description: <Rainfall Statistics>
# Assignment Name and Number: Chapter 7: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.

#January=1
#February=2
#March=3
#April=4
#May=5
#June=6
#July=7
#August=8
#September=9
#October=10
#November=11
#December=12

print("This program will provide a comprehensive set of statistics of yearly rainfall.")

rainfall=[]

for index in range(0,12):
    rain_in_month=int(input("Please enter the rainfall of a month: "))
    rainfall.insert(index,rain_in_month)


max=max(rainfall)
min=min(rainfall)
print("Month",rainfall.index(max),"had the most rainfall")
print("Month",rainfall.index(min),"had the least rainfall")


sum=0
for total in rainfall:
    sum+=total
print("The total rainfall in this year was",sum)

avg=sum/len(rainfall)
print("The average rainfall in this year was",avg)



