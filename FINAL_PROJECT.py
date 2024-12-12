# This is my Final Project
import os
tuloy = True
while tuloy == True:
    print("\n======================================================================================\n\nCode_Challenge1 --- 1 \tCode_Challenge11 --- 11 \tActivity1 --- 101 \nCode_Challenge2 --- 2 \tCode_Challenge12 --- 12 \tActivity2 --- 102 \nCode_Challenge3 --- 3 \tCode_Challenge13 --- 13 \tActivity3 --- 103 \nCode_Challenge4 --- 4 \tCode_Challenge14 --- 14 \tActivity4 --- 104 \nCode_Challenge5 --- 5 \tCode_Challenge15 --- 15 \tActivity5 --- 105 \nCode_Challenge6 --- 6 \tCode_Challenge16 --- 16\nCode_Challenge7 --- 7 \nCode_Challenge8 --- 8 \nCode_Challenge9 --- 9 \nCode_Challenge10 -- 10")
    a = int(input("\nCHOOSE ONLY ONE CHALLENGE U WANT TO OPEN (TYPE ONLY THE NUMBER): ")) 
    if a == 1:
        os.system("cls")
        def Activity1():
            print("Hello World")
        Activity1()
        continue

    elif a == 2:
        os.system("cls")
        def Activity2():
            name = input( "Please enter a name -----> " )
            print ( "Hi!" + name )
        Activity2()
        continue

    elif a == 3:
        os.system("cls")
        def Activity3():
            pangalan = input("Please input your full name here ---> ")
            fname = input("Please input your father's name here ---> ")
            mname = input("Please input your mother's name here ---> ")
            birthdate = input("Please input your birth date here ---> ")
            birthmonth = input("Please input your birthmonth here ---> ")
            birthyear = input("Please input your birthyear here ---> ")
            maritalstatus = input("Please input your maritalstatus here ---> ")
            religion = input("Please input your religion here ---> ")
            ethnicity = input("Please input your ethnicity here ---> ")
            mobile = input("Please input your mobile here ---> ")
            email = input("Please input your email here ---> ")
            gender = input("Please input your gender here ---> ")
            address = input("Please input your address here ---> ")
            age = input(" Please input your age here ---> ")
            print("\n\n\n\n\tHello, My name is,", pangalan ,"I'm", age ,"yrs old.\n\tI identify as", gender ,"\n\tMy father's name is", fname ,"\n\tMy mother's name is", mname ,"\n\tMy Bithday is in", birthmonth , birthdate , birthyear ,"\n\tI live in", address,"\n\tI am", maritalstatus ,"\n\tI am", ethnicity ,"Citizen\n\tMy mobile number is:", mobile ,"\n\tYou may contact me in my email:", email ,"\n\tThank You!!!\n\n\n")
        Activity3()
        continue

    elif a == 4:
        os.system("cls")
        def Activity4():
            number1 = eval (input("enter a number--->" ))
            number2 = eval (input("enter another number--->" ))
            answer = (number1 + number2)
            print("The sum of", number1 ,"and",number2,"is",answer)
        Activity4()
        continue

    elif a == 5:
        os.system("cls")
        def Activity5():
            print('\n\t\t\t\t\t\t=================================')
            print('\t\t\t\t\t\t|FAHRENHEIT TO CELSIUS CONVERTER|')
            print('\t\t\t\t\t\t=================================')
            temp=eval(input('\nEnter Temperature in Fahrenheit: '))
            celsius=(temp - 32) * 5/9
            print(f'\n\nThe conversion of {temp} degrees Fahrenheit is {celsius} degrees Celsius\n\nor')
            print(f'\nThe conversion of {temp} degrees Fahrenheit is {round(celsius, 2)} degrees Celsius')
        Activity5()
        continue

def Activity6():
    x = 5
    print(x)
    x = x + 10
    print(x)
    x = x +15
    print(x)
    x += 10 
    print(x)
    x+=20
    print(x)

def Activity7():
    gold = 0

    name=input('Hi, enter your name:  ')
    hasMine=input('Did you mine gold today?  ')

    if hasMine.lower() == "yes":
        gold +=1
        print(f'Hi! {name}, Today you have a total of {gold} gold')
    else:
        print(f'Hi! {name}, Today you have a total of {gold} gold')

def Activity8():
    password = input('Enter your password---> ')
    if password.lower() == "lester" :
        print('Access Granted!!!!')
        print('Enjoy using the system')
    elif password.lower() =='casipit':
        print('Access Granted!!!!')
        print('Enjoy using the system')
    else:
        print('Access Denied!!!!!')
    print('Thank you for using the system')

def Activity9():

    age=eval(input('Enter your age here--->'))

    if age >=60:
            print("You are a senior citizen")

    elif age >= 46:
            print("You are in a post adulthood")

    elif age >= 32:
            print("You are in a mid adulthood")

    elif age >= 19:
            print("You are in a early adulthood")

    elif age  >= 14:
            print("teenager")

    elif age >= 8:
            print("You are a pre teen")

    elif age > 1:
            print("You are a toddler")
     
def Activity10():
    isDLL= input('Are you a current student of DLL (yes/no):  ')

    if isDLL.lower() == 'yes':
        print('Welcome to the DLL BSIT Scholarship form')
        isCotta= input('Are you from Barangay Cotta (yes/ no):  ')

        if isCotta.lower() == 'yes':
            print('Please fillup the second form')
            isLevel=input('What is your current level right now in DLL\nF - Freshmen\nS - Sophomore\nJ - Junior\nR - Senior\nPlease input your answer')
            if isLevel.lower() == 'f':
                print('Hi Freshmen')
            elif isLevel.lower() == 's':
                print('Hi Sophomore')
            elif isLevel.lower() == 'j':
                print('Hi Junior')
            elif isLevel.lower() == 'r':
                print('Hi Senior')
            else:
                print('Invalid choice')
            isNeeded = input('Do you need this scholarship (yes/no):  ')
        
            if isNeeded.lower() == 'yes':
                print('Scholarship Granted')
            else:
                print('Thanks for stopping by')
        else:
            print('Sorry, this Scholarship grant are only for resident of Cotta')
    else:
        print('Thanks for stopping by')
     
def Activity11():
    
    for x in range (6,1,-1):
        for y in range (1, x + 1):
         print(" ",end=" ")
    for z in range(6, x, -1):
        print("*",end=" ")
    for a in range(5, x, -1):
        print("*",end=" ")
    print()
    
    for x in range (1,6):
        for y in range (1, x + 1):
            print(" ",end=" ")
        for z in range(5, x, -1):
            print("*",end=" ")
        for xx in range(6, x, -1):
            print("*",end=" ")
        print()

def Activity12():
    for cycle in range (10,0,-1):
        print(cycle)

def Activity13():
    sum = 1
    num=int(input('Enter a number: '))

    for x in range (num,0,-1):
        sum *= x
    print(f"The factorial of {num} is {sum}")

def Activity14():
    for x in range ( 0, 11,):
        print(x,end =" ")
        for y in range (0, 11):
            print("*",end = " ")
        print("")

def Activity15():
    for x in range ( 0, 11,):
        print(x,end =" ")
    for y in range (0, x):
        print("*",end = " ")
    print("")

def Activity16():
    for x in range (1,11,):
        for y in range (1, x + 1):
            print(" ",end=" ")
    for z in range(11, x, -1):
        print(" * ",end=" ")
    print()
def Activity17():
    col = eval(input("Enter number of columns---> "))
    for x in range (1, 11):
        for y in range (1, col + 1):
            print(f"{x} x {y} = {x*y}" ,end="\t")
        print()

def Activity18():
    tri = eval(input("Enter a number of triangle---> "))

    for x in range (1, 6):
        for r in range (1 , tri + 1):
            for y in range (1 , x + 1):
                print("*", end=" ")
            for z in range (6, x, -1):
                print(" ",end=" ")
        print()

def Activity19():
    tuloy = True
    while tuloy == True:
        name = input("Enter your name: ")
        if name.lower()== "stop":
            print("PROGRAM TERMINATED")
            break
            tuloy = False
        else:
            continue
def Activity20():
    import os

    isContinue = True
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another triangle (yes / no )--> ")

        if ask.lower() == "no":
            print("PROGRAM TERMINATED")
            break
            isContinue = False
        else:
            os.system('cls')
            no += 1
            for x in range (1, 6):
                for r in range (1 , no + 1):
                    for y in range (1 , x + 1):
                        print("*", end=" ")
                    for z in range (6, x, -1):
                        print(" ",end=" ")
                print()
            continue
def Activity21():
    pass
def Activity22():
    pass
def Activity23():
    pass
def Activity24():
    pass
def Activity25():
    pass
def Code_Challenge1():
    pass
def Code_Challenge2():
    pass
def Code_Challenge3():
    pass
def Code_Challenge4():
    pass
def Code_Challenge5():
    pass
def Code_Challenge6():
    pass
def Code_Challenge7():
    pass
def Code_Challenge8():
    pass
def Code_Challenge9():
    pass
def Code_Challenge10():
    pass
def Code_Challenge11():
    pass
def Code_Challenge12():
    pass
def Code_Challenge13():
    pass
def Code_Challenge14():
    pass
def Code_Challenge15():
    pass
def Code_Challenge16():
    pass

Activity13()

