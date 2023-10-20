# File: <Exercise 6 c5>
# Description: <Calories from Fat and Carbs>
# Assignment Name and Number: Chapter 5: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.

fat_consumption=int(input("Please enter the grams of fat you consumed in a day: "))
def cals_fat(grams_fat):
    calories_from_fat=grams_fat*9
    print("You consumed",calories_from_fat,"calories from fat in a day")
cals_fat(fat_consumption)

carb_consumption=int(input("Please enter the grams of carbohydrates you consumed in a day: "))
def cals_carbs(carbs_consumed):
    calories_from_carbs=carbs_consumed*4
    print("You consumed",calories_from_carbs,"calories from carbohydrates in one day")
cals_carbs(carb_consumption)





    



