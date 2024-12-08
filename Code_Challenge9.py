a = int(input('enter a number: '))
for x in range (a, 0,-1):
    for y in range(a,x,-1):
        print(" ",end=" ")
    print("* "*x)