from math import ceil
import random

# the function finds the prime factors of given prime number and returns the array of factors.
def findPrimeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i not in factors:
                factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


# the function calculates a^K mod P is prime or not and returns the calculation string result according to the situation 
def calculateValueIsPrime(K, P, a):
    # Calculate a^K mod P
    calculation = pow(a, K) % P
    if calculation == P-1:
        return "PRIME"
    elif calculation != 1 and (calculation != -1 and K< (P-1)) :
        return "COMPOSITE"
    elif calculation == -1 or (calculation == 1 and K%2 == 1):
        return "PRIME"
    else: 
        return "CONTINUE"


# the function calculates the result of primary test
def primalityTest(K, P, a):
    # calculates the result of primary test
    result_of_calculation_control = calculateValueIsPrime(K,P, a)
    # If the gotten result is one of "PRIME" | "COMPOSITE" return result,
    # else do the test with K/2
    while result_of_calculation_control == "CONTINUE" :
        if(K>2) : 
            K = int(ceil(K/2))
            result_of_calculation_control = calculateValueIsPrime(K,P,a)
        else:
            result_of_calculation_control = "FAIL"
    
    return result_of_calculation_control


# the function provides certain control to be sure gotten P is really valid for selected random a value 
def primalityTestIteration(K, P):
    for i in range(0,10):
        # Get random value from a
        a = random.randint(0,P-1)
        # do test for gotten P with random selected a
        primeControl = primalityTest(K,P,a)
        if primeControl != "PRIME":
            return False
    
    return True
    
    
# the function gets the prime value from user until it is valid.
def getPrimeValue():
    # A prime number P is taken randomly
    P = int(input("Enter the value for P: "))
    K = P-1
    # start test for gotten P
    result = primalityTestIteration(K,P)

    # If test failed, get new value until it is valid
    if result == False:
        print('P is not prime, provide a new value for P')
        return getPrimeValue()
    else:
        return P
