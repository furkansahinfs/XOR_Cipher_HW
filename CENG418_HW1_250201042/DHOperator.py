import random
from CBC import *

# the function calculates the shared key according to the given a,b,G,P values.
def calculateSharedSecretKey(a, b, G, P):
    sharedKey = int(pow(pow(G, a),b) % P)
    return sharedKey


# Get IV value from user
def getIVValue():
    IV = int(input("Enter the value for IV: "))
    return IV

# the function gets the byte array of message, shared key and initialisation value (IV)
# and do xOR operation for each byte to encrypt each byte.
def createEncryptedByteArray(byteArrayOfMessageOfUser, sharedKey,initialisation):
    arrayOfEncryptedBytes = []
    for byte in byteArrayOfMessageOfUser :
        result = doXOR(initialisation, byte, sharedKey)
        initialisation = result
        arrayOfEncryptedBytes.append(result)
    return arrayOfEncryptedBytes


# the function gets the encrypted bytes array, shared key and initialisation value (IV)
# and do xOR operation for each byte to decrypt each byte.
def createDecryptedByteArray(arrayOfEncryptedBytes,sharedKey, initialisation ):
    arrayOfDecryptedBytes = []
    for i in range(0,len(arrayOfEncryptedBytes)):
        result = doXOR(initialisation, arrayOfEncryptedBytes[i], sharedKey)
        initialisation = arrayOfEncryptedBytes[i]
        arrayOfDecryptedBytes.append(result)

    return arrayOfDecryptedBytes