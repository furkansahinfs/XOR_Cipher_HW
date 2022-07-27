import random
from GeneratorP import findPrimeFactors

def repeatedSquareMethod(P,G,expo):
    moduloResult = 1
    for i in range (0,expo):
        moduloResult = (G * moduloResult) % P
    return moduloResult

# do the generator test in the Example 2 of homework.pdf
def generatorTest(P, G, primeFactors):
    for primeFactor in primeFactors:
        expo = int((P-1)/primeFactor)
        calculation = repeatedSquareMethod(P,G, expo)
        if calculation == 1:
            return False
            
    
    return True

def generateG(P):
    # A generator number G is taken randomly
    G = random.randint(2,P-1)

    # find the prime factors to ensure that G garanties the generation.
    primeFactors = findPrimeFactors(P-1)
    generatorResult = generatorTest(P,G, primeFactors)

    # until find a valid G, do the process
    while generatorResult == False:
        G = random.randint(2,P-1)
        generatorResult = generatorTest(P,G, primeFactors)

    return G