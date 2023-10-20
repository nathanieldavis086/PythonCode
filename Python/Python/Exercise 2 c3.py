def main():
    l1=float(input("Please enter the length of your first rectangle: "))
    l2=float(input("Please enter the length of your second rectangle: "))
    w1=float(input("Please enter the width of your first rectangle: "))
    w2=float(input("Please enter the width of your second rectangle: "))
    a1=l1*w1
    a2=l2*w2
    if a1==a2:
        print("Your rectangles have equal area")
    elif a1>a2:
        print("Your first rectangle has greater area than your second")
    elif a2>a1:
        print("Your second rectangle has greater area than your first")
print("thanks for playing")
main()
