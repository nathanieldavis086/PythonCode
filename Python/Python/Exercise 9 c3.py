print("Welcome to roulette")
n=int(input("Please enter a number: "))
if n==0:
    print("Your pocket is green")
if 0<=n<=36:
    if 1<=n<=10:
        if n%2==0:
            print("Your pocket is black")
        else:
            print("Your pocket is red")
    elif 11<=n<=18:
        if n%2==0:
            print("Your pocket is red")
        else:
            print("Your pocket is black")
    elif 19<=n<=28:
        if n%2==0:
            print("Your pocket is black")
        else:
            print("Your pocker is red")
    elif 29<=n<=36:
        if n%2==0:  
            print("Your pocket is red")
        else:
            print("Your pocket is black")
else:
    print("You must enter a whole number between 0 and 36")

