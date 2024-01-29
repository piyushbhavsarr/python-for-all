#Same functionality but easy to use with more logic
while(True):
    anycharacter=input("Enter anything and see the data type of it : ")
    if(anycharacter=="quit"):
        print("You have entered quit, now quitting the program. Bye!")
        break
    else:
        print(type(eval(anycharacter)))

    