def main():
    
    s1=int(input("Please enter the score of your first test: "))
    if 0<=s1<=25:
        S1=s1*1
    else:
        print("This score is not valid")

    s2=int(input("Please enter the score of your second test: "))
    if 0<=s2<=25:
        S2=s2*1
    else:
        print("This score is not valid")
    
    m=int(input("Please enter the score of your final: "))  
    if 0<m<=50:
        m=m*1
    else:
        print("This score is not valid")
    
    if 0<=m<=25:
        print("You failed with a score of",m,"on your final")

    f=S1+S2+m
    if f<50:
        print("You failed with a score of",f,"in the class")
    elif 50<=f<=59:
        print("You passed with a score of",f,"in the class")
    elif 60<=f<=80:
        print("You got credit with a score of",f,"in the class")
    elif 80<f<=100:
        print("You got distinguished"+"with a score of",f,"in the class")
    else:
        print("error")

        
    main()
    