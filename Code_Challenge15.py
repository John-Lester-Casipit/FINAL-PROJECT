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