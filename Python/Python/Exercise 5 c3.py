mkg=int(input("Please enter a mass from 100 to 500 kilograms: "))
wn=mkg*9.8
if 100<=mkg<=500:
    print("The weight in newtons of an object with mass",mkg,"is",wn)
elif mkg>500:
    print("Your mass is too heavy")
else:
    print("Your object is too light")
    