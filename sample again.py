tuloy = True
odd = 0
even =[]

while tuloy == True:
    num = eval(input(f"Enter a number (press zero to exit the loop): "))
    if num == 'zero'.lower():
        print (f"the sum of all odd is {odd}")
        print (even)
        break
    elif num % 2 != 0:
        odd += num
    elif num % 2 == 0:
        even.append(num)