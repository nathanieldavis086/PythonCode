# get variables
month=input("Please enter a month: ")
day=int(input("Please enter a day: "))
year=int(input("Please enter a year: "))
step=int(input("Please enter the number of days to skip(1-20): "))
#January: 31
#February: 28
# March: 31
#April: 30
#May: 31
#June: 30
#July: 31
#August: 31
#September: 30
#October: 31
#November: 30
#December: 31

#set values 1-365 for dates
list_month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
if month=="January":
    num=day
elif month=="February":
    num = day+31
elif month=="March":
    num = day+59
elif month=="April":
    num = day+90
elif month=="May":
    num = day+120
elif month=="June":
    num = day+151
elif month=="July":
    num = day+181
elif month=="August":
    num = day+212
elif month=="September":
    num = day+243
elif month=="October":
    num = day+273
elif month=="November":
    num = day+304
elif month=="December":
    num = day+334
else:
    print("Please enter a valid date")

#Add the number of days to skip with the number of the day
num+=step

















#check for leap year exception
if month=="February":
    if (year % 400==0) or ((year % 4 == 0) and (year % 100 != 0)):
        February=29
    else:
        February=28