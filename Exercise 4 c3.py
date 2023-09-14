def main():
    n=int(input("Please enter a number 1-10: "))

    if 1<=n<=3:
        print("I"*n)
    elif n==4:
        print("IV")
    elif 5<=n<=8:
        a="I"*(n-5)
        print("V"+a)
    elif n==9:
        print("IX")
    elif n==10:
        print("X")
    else:
        print("domain error")
    print("thanks for playing")
main()
    

