#This fucntion is for computing factorial

def factorial(number):
    """This function again is for calculating the factorial of a number just provide a value, and it would be automatically compute the factorial"""
    fact = 1
    for x in range (0, number, -1):
        fact *= x
    print(fact)
    return fact 
