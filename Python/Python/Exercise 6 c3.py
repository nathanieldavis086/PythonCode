def main():
    day=int(input("Please enter a day(of the month): "))
    month=int(input("Please enter a month(number): "))
    year=int(input("Please enter a year(last two digits): "))

    mult=day*month
    if mult==year:
        print("Your date is magic")
    else:
        print("Your date isn't magic")




main()
