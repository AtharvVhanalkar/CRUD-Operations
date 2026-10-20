import os

val = True



while val:
    try :
        print("Press 1 for creating a file")
        print("Press 2 for Reading a file")
        print("Press 3 for Updating a file")
        print("Press 4 for deleting a file")
        print("Press other number to Exit")
        a = int(input())
    except :
        print("You can use numbers only")
    if a == 4:
        dele = input("Which file do you want to delet?(Mention with exention):- ")
        os.remove(dele)
    elif a == 1:
        name = input("What is your file name?:- ")
        f = open(name,"x")
        f.close()

    elif a == 2:
        name = input("Which file to read?:- ")
        f = open(name,"r")
        print(f.read())
        f.close()

    elif a == 3:
        name = input("Which file to Update?:- ")
        print("---------------------")
        print("You Have 2 opotions here ")
        print("1. Overwrite the file")
        print("2. Add at the end")
        print("---------------------")
        try:
            b = int(input())
            if b == 1:
                info = input("What do you want to write?:- ")
                f = open(name,"w")
                f.write(info)
                f.close()
                print("---------------------")
                print("Changes Done!")
                print("---------------------")
            elif b == 2:
                info = input("What do you want to write?:- ")
                f = open(name,"a")
                f.write(info)
                f.close()
                print("---------------------")
                print("Changes Done!")
                print("---------------------")
        except Exception as e:
            print("Error occured")  
        

    else:
        val = False
    cl = input()