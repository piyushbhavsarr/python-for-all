#Same functionality but easy to use with more logic
print("Data Types")
print("To Quit - type quit to exit/stop the program")
while(True):
    anycharacter=input("\nEnter anything and see the data type of it : ")
    if(anycharacter=="quit"):
        print("You have entered quit, now quitting the program. Bye!")
        break
    else:
        print(type(eval(anycharacter)))

'''
Outputs:
Data Types
To Quit - type quit to exit/stop the program

Enter anything and see the data type of it : 12
<class 'int'>

Enter anything and see the data type of it : 12.545
<class 'float'>

Enter anything and see the data type of it : 50/100
<class 'float'>

Enter anything and see the data type of it : "Python with Data Science"
<class 'str'>

Enter anything and see the data type of it : 'Python With Data Science'
<class 'str'>

Enter anything and see the data type of it : ["Python", "Rust", "R"]
<class 'list'>

Enter anything and see the data type of it : ("Python")
<class 'str'>

Enter anything and see the data type of it : ("Python",) 
<class 'tuple'>

Enter anything and see the data type of it : ("Python", "Nodejs")
<class 'tuple'>

Enter anything and see the data type of it : 123, 1234, 34345
<class 'tuple'>

Enter anything and see the data type of it : {"Language":"Python", "Version":"3.12.1"}
<class 'dict'>

Enter anything and see the data type of it : 12, (23,56)
<class 'tuple'>

Enter anything and see the data type of it : ([1,2,3],[23,34,56])
<class 'tuple'>

Enter anything and see the data type of it : [[12,24],[23,56]]
<class 'list'>

Enter anything and see the data type of it : b'hello'
<class 'bytes'>

Enter anything and see the data type of it : bytearray([65, 66, 67])
<class 'bytearray'>

Enter anything and see the data type of it : [1, 2, 3, 'python', True]
<class 'list'>

Enter anything and see the data type of it : quit
You have entered quit, now quitting the program. Bye!
'''

    