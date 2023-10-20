def main():
    m=int(input("Please enter a number of a month: "))
    if 1<=m<=3:
        print("Your month is in the first quarter")
    elif 4<=m<=6:
        print("Your month is in the second quarter")
    elif 7<=m<=9:
        print("Your month is in the third quarter")
    elif 10<=m<=12:
        print("Your month is in the fourth quarter")
    else:
        print("bruh")
    print("thanks for playing")


main()
