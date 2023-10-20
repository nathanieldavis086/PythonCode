# File: <Exercise 8 c5>
# Description: <Paint Job Estimator>
# Assignment Name and Number: Chapter 5: Coding Assignment
#
# Name: <Nathaniel Davis>
# GitHub: <nathanieldavis086>
#
# On my honor, <Nathaniel Davis>, this programming assignment is my own work
# and I have not provided this code to any other student.

sqfootage=int(input("Please enter the square footage of the paint job: "))
costpaint=int(input("Please enter the cost of paint per gallon: "))


def gallons_needed(squarefootage):
    gal=squarefootage/112
    print()
    print("You need",gal,"gallons of paint")
gallons_needed(sqfootage)


def labor_time(squarefootage):
    hr=squarefootage/14
    print()
    print("This job will take",hr,"hours")
labor_time(sqfootage)
    

def paint_cost(cost_paint):
    cost=sqfootage/112*cost_paint
    print()
    print("The paint for this job will cost",cost,"dollars")
    return cost
paint_cost(costpaint)

def labor_price(squarefootage):
    labor=squarefootage/14*35
    print()
    print("The labor for this job will cost",labor,"dollars")
    return labor
labor_price(sqfootage)

total=(sqfootage/14*35)+(sqfootage/112*costpaint)
print()
print("Your total cost for a paint job with",sqfootage,"square feet is",total)
