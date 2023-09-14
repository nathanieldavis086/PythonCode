vegan=input("Is anyone in your party vegan? ")

if vegan=="Yes" or vegan=="No":
    veget=input("Is anyone in your party a vegetarian? ")
    
    if veget=="Yes" or veget=="No":
        glut=input("Is anyone in your party allergic to gluten? ")
        
        if glut=="Yes" or glut=="No":
            ans=print("Based on your input your restaurant choices are: ")
            
            if vegan=="Yes":
                if veget=="Yes":
                    if glut=="Yes" or glut=="No":
                        ans="The Corner Cafe, The Chef's Kitchen"
                        print(ans)
                else:
                    if glut=="Yes":
                        ans="The Corner Cafe, The Chef's Kitchen"
                        print(ans)
                    else:
                        ans="The Corner Cafe, The Chef's Kitchen"
                        print(ans)
            else:
                if veget=="Yes":
                    if glut=="Yes":
                        ans="The Corner Cafe, The Chef's Kitchen, Main Street Pizza Co"
                        print(ans)
                    else:
                        ans="The Corner Cafe, The Chef's Kitchen, Mama's Fine Italian"
                        print(ans)
                else:
                    if glut=="Yes":
                        ans="The Corner Cafe, The Chef's Kitchen"
                        print(ans)
                    else:
                        ans="The Corner Cafe, The Chef's Kitchen, Main Street Pizza Co, Joe's Gourmet Burger, Mama's Fine Italian"
                        print(ans)



                    

                
        else:
            print("Please answer either Yes or No")    
    else:
        print("Please answer either Yes or No")
else:
    print("Please answer either Yes or No")