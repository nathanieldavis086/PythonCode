def main():
    number=int(input("Please enter a number: "))
    if number > 0:
        print("Your number is positive")
    elif number < 0:
        print("Your number is negative")
    elif number == 0:
        print("Your number is zero")
    if number % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")

    print("thanks for playing")



main()

