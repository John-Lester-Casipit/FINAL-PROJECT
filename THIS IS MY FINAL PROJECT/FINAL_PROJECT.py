    # This is my Final Project
    # JOHN LESTER F. CASIPIT
    # BSIT-1C
import os
b=input ("Would you like to enter my final project? (yes/no): ")
if b == 'yes'.lower():
    import os
    tuloy = True
    while tuloy == True:
        print("===========================================================================")
        print ("Activity  1 -- 1				Code Challenge  1 -- 101")
        print ("Activity  2 -- 2				Code Challenge  2 -- 102")
        print ("Activity  3 -- 3				Code Challenge  3 -- 103")
        print ("Activity  4 -- 4				Code Challenge  4 -- 104")
        print ("Activity  5 -- 5				Code Challenge  5 -- 105")
        print ("Activity  6 -- 6				Code Challenge  6 -- 106")
        print ("Activity  7 -- 7				Code Challenge  7 -- 107")
        print ("Activity  8 -- 8				Code Challenge  8 -- 108")
        print ("Activity  9 -- 9				Code Challenge  9 -- 109")
        print("Activity 10 -- 10				Code Challenge 10 -- 110")
        print("Activity 11 -- 11				Code Challenge 11 -- 111")
        print("Activity 12 -- 12				Code Challenge 12 -- 112")
        print("Activity 13 -- 13				Code Challenge 13 -- 113")
        print("Activity 14 -- 14				Code Challenge 14 -- 114")
        print("Activity 15 -- 15				Code Challenge 15 -- 115")
        print("Activity 16 -- 16				Code Challenge 16 -- 116")
        print("Activity 17 -- 17")
        print("Activity 18 -- 18")
        print("Activity 19 -- 19")
        print("Activity 20 -- 20")
        print("Activity 21 -- 21")
        print("Activity 22 -- 23")
        print("Activity 23 -- 23")
        print("Activity 24 -- 24")
        print("Activity 25 -- 25                                EXIT -- 0")
        print("===========================================================================")
        a = int(input("\nCHOOSE ONLY ONE CHALLENGE U WANT TO OPEN (TYPE ONLY THE NUMBER): ")) 
        if a == 1:
            os.system("cls")
            def Activity1():
                print()
                print("\t\tACTIVITY 1")
                print('|====================================================|')
                print("|This is the example on how you print                |")
                print('|                                                    |')
                print('|input: print("Hello World")                         |')
                print('|output: Hello World"                                |')
                print('|====================================================|')
                print()
            Activity1()
            continue

        elif a == 2:
            os.system("cls")
            def Activity2():
                print()
                print("\t\tACTIVITY 2")
                print('===========================================================')
                print("THIS IS THE EXAMPLE ON HOW YOU PRINT AND ADD ONE VARIABLE")
                name = input( "Please enter a name -----> " )
                print ( "Hi!" + name )
                print()
                print ('INPUT:  name = input( "Please enter a name -----> ") ')
                print ('OUTPUT: ( "Hi!" + name )')
                print('===========================================================')
            Activity2()
            continue

        elif a == 3:
            os.system("cls")
            def Activity3():
                print()
                print("\t\tACTIVITY 3")
                print('===========================================================')
                print()
                print("THIS IS THE EXAMPLE ON HOW YOU PRINT WITH MULTIPLE VARIABLES")
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
                age = input("Please input your age here ---> ")
                print()
                print()
                print('===========================================================')
                print("\tHello, My name is,", pangalan ,"I'm", age ,"yrs old.\n\tI identify as", gender ,"\n\tMy father's name is", fname ,"\n\tMy mother's name is", mname ,"\n\tMy Bithday is in", birthmonth , birthdate , birthyear ,"\n\tI live in", address,"\n\tI am", maritalstatus ,"\n\tI am", ethnicity ,"Citizen\n\tMy mobile number is:", mobile ,"\n\tYou may contact me in my email:", email ,"\n\tThank You!!!")
                print('===========================================================')
            Activity3()
            continue

        elif a == 4:
            os.system("cls")
            def Activity4():
                print()
                print("\t\tACTIVITY 4")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF ADDING THE VALUE OF VARIABLE")
                number1 = eval (input("enter a number--->" ))
                number2 = eval (input("enter another number--->" ))
                answer = (number1 + number2)
                print("The sum of", number1 ,"and",number2,"is",answer)
                print('===========================================================')
            Activity4()
            continue

        elif a == 5:
            os.system("cls")
            def Activity5():
                print()
                print("\t\tACTIVITY 5")
                print('===========================================================')
                print("THIS FUNCTION IS THE EXAMPLE OF CONVERSION CELSUIS TO FARENHEIT")
                print('\n\t\t\t\t\t\t=================================')
                print('\t\t\t\t\t\t|FAHRENHEIT TO CELSIUS CONVERTER|')
                print('\t\t\t\t\t\t=================================')
                temp=eval(input('\nEnter Temperature in Fahrenheit: '))
                celsius=(temp - 32) * 5/9
                print(f'\n\nThe conversion of {temp} degrees Fahrenheit is {celsius} degrees Celsius\n\nor')
                print(f'\nThe conversion of {temp} degrees Fahrenheit is {round(celsius, 2)} degrees Celsius')
            Activity5()
            continue

        elif a == 6:
            os.system("cls")
            def Activity6():
                print()
                print("\t\tACTIVITY 6")
                print('===========================================================')
                print("THIS FUNCTION IS THE EXAMPLE OF THE HOW THE DATA IN VARIABLE CHANGES")
                print()
                print("INPUT: \nx = 5\nprint(x)\nx = x + 10\nprint(x)\nx = x +15\nprint(x)\nx += 10\nprint(x)\nx+=20\nprint(x)")
                print()
                print("OUTPUT:")
                print()
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
                print('===========================================================')
            Activity6()
            continue
        elif a == 7:
            os.system("cls")
            def Activity7():
                print()
                print("\t\tACTIVITY 7")
                print('===========================================================')
                print('THIS IS THE EXAMPLE OF HAVE AN NESTED CONDITION AND USE OPERATORS')
                print('===========================================================')
                print()
                gold = 0
                name=input('Hi, enter your name:  ')
                hasMine=input('Did you mine gold today?  ')
                if hasMine.lower() == "yes":
                    gold +=1
                    print(f'Hi! {name}, Today you have a total of {gold} gold')
                    print('===========================================================')
                else:
                    print(f'Hi! {name}, Today you have a total of {gold} gold')
                    print('===========================================================')
            Activity7()
            continue

        elif a == 8:
            os.system("cls")
            def Activity8():
                print()
                print("\t\tACTIVITY 8")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF GIVE SOME STRING NESTED CONDITION THRU STRING AND ENTERING PASSWORD")
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
            Activity8()
            continue

        elif a == 9:
            os.system("cls")
            def Activity9():
                print()
                print()
                print("\t\tACTIVITY 9")
                print('===========================================================')
                print("THIS IS THE EXAMPLE ON HOW YOU USE THE ARITHMETHIC OPERATORS")
                print("THIS PROGRAM IDENTIFY YOUR AGE")
                print()
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
            Activity9()
            continue

        elif a == 10:
            os.system("cls")
            def Activity10():
                print()
                print()
                print("\t\tACTIVITY 10")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF USING THE NESTED CONDITION INSIDE THE NESTEDD CONDITION")
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
            Activity10()
            continue

        elif a == 11:
            os.system("cls")
            def Activity11():
                print()
                print()
                print("\t\tACTIVITY 11")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF THE FOR LOOP")
                for me in range (1 , 10):
                    print(me, 'HELLO WORLD')
                    print('===========================================================')
            Activity11()
            continue

        elif a == 12:
            os.system("cls")
            def Activity12():
                print()
                print()
                print("\t\tACTIVITY 12")
                print("THIS IS THE EXAMPLE OF THE FOR LOOP")
                for cycle in range (10,0,-1):
                    print(cycle)
                    print('===========================================================')
            Activity12()
            continue

        elif a == 13:
            os.system("cls")
            def Activity13():
                print()
                print()
                print("\t\tACTIVITY 13")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF THE FACTORIAL ")
                sum = 1
                num=int(input('Enter a number: '))

                for x in range (num,0,-1):
                    sum *= x
                print(f"The factorial of {num} is {sum}")
                print('===========================================================')
            Activity13()
            continue


        elif a == 14:
            os.system("cls")
            def Activity14():
                print()
                print()
                print("\t\tACTIVITY 14")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF FOR LOOP WITH TWO VARIABLES")
                for x in range ( 0, 11,):
                    print(x,end =" ")
                    for y in range (0, 11):
                        print("*",end = " ")
                    print("")
                print('===========================================================')
            Activity14()
            continue

        elif a == 15:
            os.system("cls")
            def Activity15():
                print()
                print()
                print("\t\tACTIVITY 15")
                print('===========================================================')
                print("THIS IS THE  ANOTHE EXAMPLE OF FOR LOOP WITH TWO VARIABLES")
                for x in range ( 0, 11,):
                    print(x,end =" ")
                    for y in range (0, x):
                        print("*",end = " ")
                    print("")
            Activity15()
            continue

        elif a == 16:
            os.system("cls")
            def Activity16(Activity16):
                print()
                print()
                print("\t\tACTIVITY 16")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF FOR LOOP WITH NESTED CONDITION")
                print()
                print()
                for x in range (1,11):
                    for y in range (1, x + 1):
                        print(" ",end=" ")
                    for z in range(11, x, -1):
                        print(" * ",end=" ")
                    print()
            Activity16(Activity16)
            continue

        elif a == 17:
            os.system("cls")
            def Activity17():
                print()
                print()
                print("\t\tACTIVITY 17")
                print('===========================================================')
                print("MULTIPLICATION TABLE")
                col = eval(input("Enter number of columns---> "))
                for x in range (1, 11):
                    for y in range (1, col + 1):
                        print(f"{x} x {y} = {x*y}" ,end="\t")
                    print()
            Activity17()
            continue

        elif a == 18:
            os.system("cls")
            def Activity18():
                print()
                print()
                print("\t\tACTIVITY 18")
                print('===========================================================')
                print("THIS IS THE  ANOTHE EXAMPLE OF FOR LOOP WITH TWO VARIABLES")
                tri = eval(input("Enter a number of triangle---> "))

                for x in range (1, 6):
                    for r in range (1 , tri + 1):
                        for y in range (1 , x + 1):
                            print("*", end=" ")
                        for z in range (6, x, -1):
                            print(" ",end=" ")
                    print()
            Activity18()
            continue
        
        elif a == 19:
            os.system("cls")
            def Activity19():
                print()
                print()
                print("\t\tACTIVITY 19")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF WHILE LOOP")
                tuloy = True
                while tuloy == True:
                    name = input('Enter your name:(type "stop" to terminate the loop) ')
                    if name.lower()== "stop":
                        print("PROGRAM TERMINATED")
                        break
                        tuloy = False
                    else:
                        continue
            Activity19()
            continue

        elif a == 20:
            os.system("cls")
            def Activity20():
                print()
                print()
                print("\t\tACTIVITY 20")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF WHILE LOOP AND FOR LOOP COMBINED")
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
            Activity20()
            continue

        elif a == 21:
            os.system("cls")
            def Activity21():
                print()
                print()
                print("\t\tACTIVITY 21")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF DEFINING A FUNCTION")
                def pang_hello():
                    print("HELLO IT1C")
                
                def pang_hello_V2(name):
                    print(f"Hello {name}")
                
                tuloy = True
                while tuloy == True:
                    ask = input('Please provide a name -->(type "stop" to terminate the loop) ')
                    if ask.lower() != "stop":
                        pang_hello_V2(ask)
                    else:
                        break

            Activity21()
            continue

        elif a == 22:
            os.system("cls")
            def Activity22():
                print()
                print()
                print("\t\tACTIVITY 22")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF COMBINATION OF LISTING AND WHILE LOOP")
                tuloy = True
                pangalan = []
                while tuloy == True:
                    name = input('What name would you like to add?(type "stop" to terminate the loop) ')
                    if name.lower() == "stop":
                        print(pangalan)
                        print(f"You have entered {len(pangalan)} names! ")
                        break
                    else:
                        pangalan.append(name)
            Activity22()
            continue

        elif a == 23:
            os.system("cls")
            def Activity23():
                print()
                print()
                print("\t\tACTIVITY 23")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF DOCUMENTARY STRING")
                #This function is for computing factorial
                def factorial(number):
                    """This function again is for calculating the factorial of a number just provide a value, and it would be automatically compute the factorial"""
                    fact = 1
                    for x in range (number, 0, -1):
                        fact *= x
                    return fact 
                print("INPUT:")
                print('def factorial(number):')
                print('\t"""This function again is for calculating the factorial of a number just provide a value, and it would be automatically\n compute the factorial"""')
                print('fact = 1\nfor x in range (number, 0, -1):\n\tfact *= x\nreturn fact')
            Activity23()
            continue

        elif a == 24:
            os.system("cls")
            def Activity24():
                print()
                print()
                print("\t\tACTIVITY 24")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF MODULES AND IMPOTATION VARIABLE FROM ANOTHER FILE")
                #MODULES
                global sum
                global num

                from Activity13 import sum ,num
                global sum
                print(f"The factorial of {num} is {sum}")
                
            Activity24()
            continue
            
        elif a == 25:
            os.system("cls")
            def Activity25():
                print()
                print()
                print("\t\tACTIVITY 25")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF LISTING")
                #LIST
                fruits1 = "apple"
                fruits2 = "banana"
                fruits3 = "orange"
                fruits4 = "star apple"
                fruits5 = "guyabano"
                fruits = ["apples", "banana", "orange", "star apple", "guyabano"]
                print(f"\n\t{fruits}")
                print(f"\n\tMy favorite childhood fruit is {fruits[1]}")
                fruits.append("longgan")
                print(f"\n\t{fruits}")
            Activity25()
            continue

        elif a == 101:
            os.system("cls")
            def Code_Challenge1():
                print()
                print()
                print("\tTHIS IS CODE CHALLENGE 1")
                print('===========================================================')
                print("THIS IS THE EXAMPLE ON HOW YOU USE ESCAPE SEQUENCE")
                print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\b\t*\n\n\n\n\t\t\t\t\t\t\t\t\t     \t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t\t   \t*\t*\t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t \t*\t*\t*\t*\t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t\t   \t*\t*\t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t\t\t     \t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t*")
            Code_Challenge1()
            continue

        elif a == 102:
            os.system("cls")
            def Code_Challenge2():
                print()
                print()
                print("\tTHIS IS CODE CHALLENGE 2")
                print('===========================================================')
                print("THIS IS THE EXAMPLE ON HOW YOU USE ESCAPE SEQUENCE AND VARIABLE")
                name = input("please enter your name ---->")
                print(f"\n\n\n\t\t\t\t\t\t\t\t\t\t\t\b\t*\n\n\n\n\t\t\t\t\t\t\t\t\t      \t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t\t   \t*\t*\t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t \t*                  {name}                 \t*\n\n\n\n\t\t\t\t\t\t\t\t   \t*\t*\t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t\t\t     \t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t*")
            Code_Challenge2()
            continue

        elif a == 103:
            os.system("cls")
            def Code_Challenge3():
                print()
                print()
                print("\tTHIS IS CODE CHALLENGE 2")
                print('===========================================================')
                print("THIS IS THE EXAMPLE ON HOW YOU PRINT WITH MULTIPLE VARIABLES")
                name = input("Please input your name here ---> ")
                fname = input("Please input your fname here ---> ")
                mname = input("Please input your mname here ---> ")
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


                print("\n\n\n\n\tHello, My name is,", name ,"I'm", age ,"yrs old.\n\tI identify as", gender ,"\n\tMy father's name is", fname ,"\n\tMy mother's name is", mname ,"\n\tMy Bithday is in", birthmonth , birthdate , birthyear ,"\n\tI live in", address,"\n\tI am", maritalstatus ,"\n\tI am", ethnicity ,"Citizen\n\tMy mobile number is:", mobile ,"\n\tYou may contact me in my email:", email ,"\n\tThank You!!!\n\n\n")
            Code_Challenge3()
            continue

        elif a == 104:
            os.system("cls")
            def Code_Challenge4():
                print()
                print()
                print("\tTHIS IS CODE CHALLENGE 4")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF USING SUBJECT OPERATORS")
                no1 = eval(input("choose a number---> "))
                no2 = eval(input("choose another number ----> "))
                ans1 = (no1 + no2)
                ans2 = (no1 - no2)
                ans3 = (no1 * no2)
                ans4 = (no1 / no2)
                ans5 = (no1 % no2)
                ans6 = (no1 ** no2)
                ans7 = (no1 // no2)

                print("the sum of", no1 ,"and", no2 ,"is", ans1 ,)
                print("the difference of", no1 ," and", no2 ,"is", ans2 ,)
                print("the product of", no1 ,"and", no2 ,"is", ans3 ,)
                print("the qoutient of", no1 ,"and", no2 ,"is", ans4 ,)
                print("the remainder of", no1 ,"and", no2 ,"is", ans5 ,)
                print("the exponent of", no1 ,"and", no2 ,"is", ans6 ,)
                print("the floor division of", no1 ,"and", no2 ,"is", ans7 ,)
            Code_Challenge4()
            continue

        elif a == 105:
            os.system("cls")
            def Code_Challenge5():
                print()
                print()
                print("\tTHIS IS CODE CHALLENGE 5 ")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF THE BREAKDOWN OF ONE OF THE VALUE OF VARIABLES")
                name=input("enter a name:")
                amount=eval(input("enter amount to deposit:"))


                a1=amount//1000
                a2=amount%1000

                b1=a2//500
                b2=a2%500

                c1=b2//200
                c2=b2%200

                d1=c2//100
                d2=c2%100

                e1=d2//50
                e2=d2%50

                f1=e2//20
                f2=e2%20

                g1=f2//10
                g2=f2%10

                h1=g2//5
                h2=g2%5

                i1=h2//1
                i2=h2%1

                print("Hi,",name,"The breakdown of your deposit",amount,"is:")
                print("1,000--",a1,)
                print("  500--",b1,)
                print("  200--",c1,)
                print("  100--",d1,)
                print("   50--",e1,)
                print("   20--",f1,)
                print("   10--",g1,)
                print("    5--",h1,)
                print("    1--",i1,)
            Code_Challenge5()
            continue

        elif a == 106:
            os.system("cls")
            def Code_Challenge6():
                print()
                print()
                print("\tTHIS IS CODE CHALLENGE 6 ")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF THE USE OF ASSIGNMENT OPERATORS")
                prelim=eval(input('Enter your grade in prelim :'))
                midterm=eval(input('Enter your grade in midterm :'))
                semifinal=eval(input('Enter your grade in semifinal :'))
                final=eval(input('Enter your grade in final :'))
                quiz=eval(input('Enter your grade in quiz :'))
                proj=eval(input('Enter your grade in project :'))

                if (prelim >= 65 and prelim <=100) and (midterm >= 65 and midterm <=100) and (semifinal >=65 and semifinal <=100) and (final >= 65 and final <=100) and (quiz >= 65 and quiz <=100) and (proj >= 65 and proj <=100):
                    
                    grade = (prelim * .15) + (midterm * .15) + (semifinal * .15) + (final * .15) + (quiz * .25) + (proj * .15)

                    if grade >= 75:
                        print('CONGRATULATONS, YOU PASSED WITH AN AVERAGE GRADE OF',grade,)

                    else:
                        print('SORRY YOU FAILED')
                        print(f'your average is {grade}')
                else:
                    print('INVALID GRADE')
            Code_Challenge6()
            continue

        elif a == 107:
            os.system("cls")
            def Code_Challenge7():
                print()
                print()
                print("\tTHIS IS CODE CHALLENGE 7 ")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF THe BREAKDOWN OF ONE OF THE VALUE OF VARIABLES")
                A = input("DID YOU BUY A MEAT GOOD/s (yes/no)? ")
                if A.upper() == "YES":
                    print('\nTHIS ARE THE LIST OF AVAILABLE MEAT GOODS')
                    print('===========================================')
                    print('Pork ------- 300php/kilo')
                    print('Chicken ---- 250php/kilo')
                    print('Beef ------- 400php/kilo')
                    print('Rabbit ----- 250php/kilo')
                    print('Tocino ----- 100php/kilo')
                    print('Bacon ------ 120php/kilo')
                    print('Bologna -----100php/kilo')
                    quan1= eval(input("\nHow many kilos of Pork meat you want to buy? "))
                    pork=quan1 * 300

                    quan2= eval(input("\nHow many kilos of Chicken meat you want to buy? "))
                    chicken=quan2 * 250

                    quan3= eval(input("\nHow many kilos of Beef meat you want to buy? "))
                    beef=quan3 * 400

                    quan4= eval(input("\nHow many kilos of Rabbit meat you want to buy? "))
                    rabbit=quan4 * 250

                    quan5= eval(input("\nHow many kilos of Tocino meat you want to buy? "))
                    tocino=quan5 * 100

                    quan6= eval(input("\nHow many kilos of Bacon meat you want to buy? "))
                    bacon=quan6 * 120

                    quan7= eval(input("\nHow many kilos of Bologna meat you want to buy? "))
                    bologna=quan7 * 100

                    total= pork+chicken+beef+rabbit+tocino+bacon+bologna
                    tax=(pork*0.123) or (chicken*0.123) or (beef*0.123) or (rabbit*0.123) or (tocino*0.123) or (bacon*0.123) or (bologna*0.123)
                    total_and_tax= (total + tax)
                    print()
                    age = input("Are you a Senior Citizen(yes/no)? ")
                    if age.lower() =='yes':
                        disc=round(total*0.052)
                        print(f"Hi, customer, you purhased a \n{quan1}kilo of Pork meat\n{quan2}kilo of Chicken meat\n{quan3}kilo of Beef meat\n{quan4}kilo of Rabbit meat\n{quan5}kilo of Tocino meat\n{quan6}kilo of Bacon meat\n{quan7}kilo of Bologna meat\nwith the total price of {total}php plus a 12.3% tax ({tax}php) and with a discount of 5.2% ({disc}php)")
                    
                    else:
                        disc=0
                        print(f"Hi, customer, you purhased a \n{quan1}kilo of Pork meat\n{quan2}kilo of Chicken meat\n{quan3}kilo of Beef meat\n{quan4}kilo of Rabbit meat\n{quan5}kilo of Tocino meat\n{quan6}kilo of Bacon meat\n{quan7}kilo of Bologna meat with the total price of {total}php plus a 12.3% tax(",tax,")")
                    print()
                    E = float(input("Amount Given: "))
                    print()
                    if E>= total_and_tax:
                        change = round(E - total_and_tax + disc)
                        print('=================RECEIPT===================')
                        print('Qty.    Description           Amount')
                        print(f'{quan1}x ----- PORK MEAT.........{pork}php')
                        print(f'{quan2}x ----- CHICKEN MEAT......{chicken}php')
                        print(f'{quan3}x ----- BEEF MEAT.........{beef}php ')
                        print(f'{quan4}x ----- RABBIT MEAT.......{rabbit}php')
                        print(f'{quan5}x ----- TOCINO MEAT.......{tocino}php')
                        print(f'{quan6}x ----- BACON MEAT........{bacon}php')
                        print(f'{quan7}x ----- BOLOGNA MEAT......{bologna}php')
                        print()
                        print(f'SUBTOTAL...................{total}php')
                        print(f'TAX(12.3%).................{tax}php')
                        print(f'TOTAL......................{total_and_tax}php')
                        print(f'PAY AMOUNT.................{E}php')
                        print(f'DISCOUNT(5.2%).............{disc}php') 
                        print(f'CHANGE.....................{change}php')
                        print()
                        print("==THANK YOU COME AGAIN!!==")
                    else:
                        E< total_and_tax
                        print("Insufficient Amount")
                else :
                    print("Thankyou for stopping by!")
            Code_Challenge7()
            continue
        
        elif a == 108:
            os.system("cls")
            def Code_Challenge8():
                print()
                print()
                print("\tTHIS IS CODE CHALLENGE 8 ")
                print('===========================================================')
                print("THIS IS THE EXAMPLE COMBINATION OF LOOP AND ASSIGNMENT OPERATORS")
                sum = 0
                odd = 0
                even = 0
                for x in range (1,11):
                    num=int(input(f'enter number {x}: '))
                    sum += num
                    if num % 2 == 0:
                        odd += num
                    else:
                        even += num


                print(f'The sum of all numbers given is {sum}')
                print(f'The odd of all numbers given is {odd}')
                print(f'The even of all numbers given is {even}')
            Code_Challenge8()
            continue

        elif a == 109:
            os.system("cls")
            def Code_Challenge9():
                print()
                print()
                print("\tTHIS IS CODE CHALLENGE 9 ")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF  FOR LOOP")
                a = int(input('enter a number: '))
                for x in range (a, 0,-1):
                    for y in range(a,x,-1):
                        print(" ",end=" ")
                    print("* "*x)
            Code_Challenge9()
            continue

        elif a == 110:
            os.system("cls")
            def Code_Challenge10():
                print()
                print()
                print("\tTHIS IS CODE CHALLENGE 10 ")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF  FOR LOOP WITH MULTIPLE VARIABLE")
                for x in range (6,0,-1):
                    for y in range (1, x + 1):
                        print(" ",end=" ")
                    for z in range(6, x, -1):
                        print("^",end=" ")
                    for a in range(6, x, -1):
                        print("*",end=" ")
                    print()
        
                for x in range (1,6):
                    for y in range (1, x + 1):
                        print(" ", end=" ")
                    for z in range(6, x, -1):
                        print("^",end=" ")
                    for xx in range(6, x, -1):
                        print("*",end=" ")
                    print()
            Code_Challenge10()
            continue

        elif a == 111:
            os.system("cls")
            def Code_Challenge11():
                print()
                print()
                print("\tTHIS IS CODE CHALLENGE 11 ")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF  FOR LOOP")
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
            Code_Challenge11()
            continue

        elif a == 112:
            os.system("cls")
            def Code_Challenge12():
                print()
                print()
                print("\tTHIS IS CODE CHALLENGE 12 ")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF  FOR LOOP")
                for x in range (6,0,-1):
                    for y in range (1, x + 1):
                        print(" ",end=" ")
                    for z in range(7, x, -1):
                        print("*",end=" ")
                    for a in range(6, x, -1):
                        print("*",end=" ")
                    print()
                
                for x in range (1,6):
                    for y in range (1, 6):
                        print(" ", end=" ")
                    for z in range(1, 4):
                        print("*",end=" ")
                    print()
            Code_Challenge12()
            continue

        elif a == 113:
            os.system("cls")
            def Code_Challenge13():
                print()
                print()
                print("\tTHIS IS CODE CHALLENGE 13 ")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF  FOR LOOP")
                for x in range (1,7):
                    for y in range (6, x , -1):
                        print(" ",end=" ")
                    for z in range(x, 1, -1):
                        print(z,end=" ")
                    for a in range(1, x + 1):
                        print(a,end=" ")
                    print()
                
                for x in range (5,0,-1):
                    for y in range (6, x, -1):
                        print(" ",end=" ")
                    for z in range(x, 1, -1):
                        print(z,end=" ")
                    for xx in range(1,x + 1):
                         print(xx,end=" ")
                    print()
            Code_Challenge13()
            continue

        elif a == 114:
            os.system("cls")
            def Code_Challenge14():
                print()
                print()
                print("\tTHIS IS CODE CHALLENGE 14 ")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF WHILE LOOP")
                tuloy = True
                a = 0
                while tuloy == True:
                    number = eval(input("Enter a number--->(press 0 to stop the program)  "))
                    if number == 0:
                        print("Program Terminated")
                        print(f"The total of the number you enter is {a}")
                        break

                    else:
                        a += number
                        continue
            Code_Challenge14()
            continue

        elif a == 115:
            os.system("cls")
            def Code_Challenge15():
                print()
                print()
                print("\tTHIS IS CODE CHALLENGE 8 ")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF COMBINATION OF WHILE LOOP AND FOR LOOP")
                import os
                a = True
                no = 0
                while a == True:
                    b = input('Would you like to add triangle ("yes" or "no" ): ')
                    if b.lower() == "no":
                        print("Program Terminated")
                        break
                        a = False
                    elif b.lower() == "yes":
                        os.system('cls')
                        no += 1
                        for x in range (1, 6):
                            for r in range (1 , no + 1):    
                                for y in range (1 , x + 1):
                                    print("*", end=" ")
                                for z in range (6, x, -1):
                                    print(" ",end=" ")
                            print()
                    else:
                        print('Invalid, answer must be ("yes" or "no")')
                        continue
            Code_Challenge15()
            continue
        
        elif a == 116:
            os.system("cls")
            def Code_Challenge16():
                print()
                print()
                print("\tTHIS IS CODE CHALLENGE 16 ")
                print('===========================================================')
                print("THIS IS THE EXAMPLE OF DEFINING A FUNCTION")
                accounts = {}

                def Create_Account():
                    Account_Name = input("Enter account name: ")
                    if Account_Name in accounts:
                        print("Account already exists!")
                    else:
                        accounts[Account_Name] = 0
                        print(f"Account created successfully for {Account_Name}.")


                def denomination(amount):
                    print("\nDenomination Breakdown:")
                    answer1 = amount // 1000
                    ans1 = amount % 1000
                    answer2 = ans1 // 500
                    ans2 = ans1 % 500
                    answer3 = ans2 // 200
                    ans3 = ans2 % 200
                    answer4 = ans3 // 100
                    ans4 = ans3 % 100
                    answer5 = ans4 // 50
                    ans5 = ans4 % 50
                    answer6 = ans5 // 20
                    ans6 = ans5 % 20
                    answer7 = ans6 // 10
                    ans7 = ans6 % 10
                    answer8 = ans7 // 5
                    ans8 = ans7 % 5
                    answer9 = ans8 // 1
                    ans9 = ans8 % 1


                    print(answer1,"-1000")
                    
                    print(answer2,"-500")

                    print(answer3,"-200")

                    print(answer4,"-100")

                    print(answer5,"-50")

                    print(answer6,"-20")

                    print(answer7,"-10")

                    print(answer8,"-5")

                    print(answer9,"-1")


                def Deposit():
                    Account_Name = input("Enter your account name: ")
                    if Account_Name in accounts:
                        try:
                            amount = int(input("Enter amount to deposit : "))
                            if amount > 0:
                                accounts[Account_Name] += amount
                                print(f"Deposited {amount} successfully. New balance: {accounts[Account_Name]}")
                                denomination(amount)
                            else:
                                print("Amount must be positive!")
                        except ValueError:
                            print("Invalid input! Please enter a whole number.")
                    else:
                        print("Account not found!")



                def Check_Balance():
                    username = input("Enter your username: ")
                    if username in accounts:
                        print(f"Your balance: {accounts[username]}")
                    else:
                        print("ACCOUNT NOT FOUND!")



                def Withdraw():
                    username = input("Enter your username: ")
                    if username in accounts:
                        try:
                            amount = int(input("Enter amount to withdraw (whole numbers only): "))
                            if 0 < amount <= accounts[username]:
                                accounts[username] -= amount
                                print(f"Withdrawn {amount} successfully. Remaining balance: {accounts[username]}")
                                denomination(amount)
                            else:
                                print("Insufficient Amount!")
                        except ValueError:
                            print("Invalid input! Please enter a exact amount.")
                    else:
                        print("ACCOUNT NOT FOUND!")


                def options():
                    while True:
                        print("\n\tWELCOME TO\nTELLYBOOOGHHSS BANKING SYSTEM")
                        print("A. Create a New Account")
                        print("B. Deposit")
                        print("C. Withdraw Money")
                        print("D. Check Balance")
                        print("E. Exit")
                        choice = input("Choose an option (A - E): ")

                        if choice == 'A':
                            Create_Account()
                        elif choice == 'B':
                            Deposit()
                        elif choice == 'C':
                            Withdraw()
                        elif choice == 'D':
                            Check_Balance()
                        elif choice == 'E' or "Exit":
                            print("Thank you for using the Banking System!")
                            break
                        else:
                            print("Invalid option. Please try again.")

                            options()
            Code_Challenge16()
            continue
        elif a == 0:
            print("THANK YOU FOR VISITING MY FINAL PROJECT")
            break
        else:
            print("INVALID INPUT")