def balik_menu():
    global tuloy  # Make sure we're modifying the global tuloy variable
    while True:
        balik = input("BACK TO MAIN MENU (YES/NO):").lower()
        if balik == 'yes':
            break
        elif balik == 'no':
            print("OKAY THANK YOU")
            tuloy = False  # Set tuloy to False to terminate the loop and stop the program
            break
        else:
            print("Invalid input. Please answer with 'YES' or 'NO'.") 

b = input("Would you like to enter my final project? (yes/no): ").lower()
if b == 'yes':
    import os
    tuloy = True  # Initialize the loop control variable
    while tuloy:
        print("===========================================================================")
        print("Activity  1 -- 1				Code Challenge  1 -- 101")
        print("Activity  2 -- 2				Code Challenge  2 -- 102")
        print("Activity  3 -- 3				Code Challenge  3 -- 103")
        print("Activity  4 -- 4				Code Challenge  4 -- 104")
        print("Activity  5 -- 5				Code Challenge  5 -- 105")
        print("Activity  6 -- 6				Code Challenge  6 -- 106")
        print("Activity  7 -- 7				Code Challenge  7 -- 107")
        print("Activity  8 -- 8				Code Challenge  8 -- 108")
        print("Activity  9 -- 9				Code Challenge  9 -- 109")
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
            balik_menu()

        elif a == 2:
            os.system("cls")
            def Activity2():
                print()
                print("\t\tACTIVITY 2")
                print('===========================================================')
                print("THIS IS THE EXAMPLE ON HOW YOU PRINT AND ADD ONE VARIABLE")
                name = input("Please enter a name -----> ")
                print("Hi!" + name)
                print()
                print('INPUT:  name = input("Please enter a name -----> ")')
                print('OUTPUT: ( "Hi!" + name )')
                print('===========================================================')
            Activity2()
            balik_menu()

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
                print("\tHello, My name is,", pangalan, "I'm", age, "yrs old.\n\tI identify as", gender, "\n\tMy father's name is", fname, "\n\tMy mother's name is", mname, "\n\tMy Birthday is in", birthmonth, birthdate, birthyear, "\n\tI live in", address, "\n\tI am", maritalstatus, "\n\tI am", ethnicity, "Citizen\n\tMy mobile number is:", mobile, "\n\tYou may contact me in my email:", email, "\n\tThank You!!!")
                print('===========================================================')
            Activity3()
            balik_menu()

        # ... (Other activities follow the same pattern as above)

        elif a == 25:
            print("Goodbye!")
            tuloy = False  # Exit the loop and terminate the program

        # Check for exit command '0'
        elif a == 0:
            print("Goodbye!")
            tuloy = False  # Exit the loop and terminate the program
