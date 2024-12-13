tuloy = True
odd = 0
even =[]

while tuloy == True:
    num = eval(input("Enter a number (press 0 to exit the loop)"))
    if num == 0:
        print (f"the sum of all odd is {odd}")
        print (even)
        break
    elif num % 2 != 0:
        odd += num
    elif num % 2 == 0:
        even.append(num)