from GeneratorP import *
from GeneratorG import *
from Users import *
from DHOperator import *
from CBC import *

def main():
    # get valid prime value from user
    P = getPrimeValue()
    print("P : ", P)

    # get valid generator according to given P
    G = generateG(P)
    print ('G : ', G)
    
    userName1 = "Alice"
    userName2 = "Bob"
    # get private keys from User A and User B
    a = getUserPrivateValue(userName1)
    b = getUserPrivateValue(userName2)

    # calculate sharedSecretKey 
    sharedKey = calculateSharedSecretKey(a,b,G,P)

    # get IV value from user
    IV = getIVValue()

    sendMessage(userName1,userName2, IV, sharedKey)
    sendMessage(userName2, userName1, IV, sharedKey)
    input("Press enter to close program")

# just print the encoded byte array as string
# not acting the process of encryption or decryption
# because of byte values > 256, I do the mod operation to get string
def byteArrayToString(byteArray):
    str = ""
    for i in byteArray:
        str += chr(i%256)
       
    return str

# the function do the message send process that encrypt and decrypt the message
def sendMessage(senderUser, receiverUser, IV, sharedKey):
    print("\n")
    # get message from sender user
    messageOfUser = getUserMessage(senderUser)

    #convert gotten message to byte array
    byteArrayOfMessageOfUser = getByteArrayOfMessage(messageOfUser)

    initialisation = IV

    # do encryption process and get array of encrypted bytes
    arrayOfEncryptedBytes = createEncryptedByteArray(byteArrayOfMessageOfUser, sharedKey, initialisation)
    print("Encrypted message of " + messageOfUser + " that User " + senderUser + " sends : " + byteArrayToString(arrayOfEncryptedBytes))
    
    initialisation = IV

    # do decryption process and get array of decrypted bytes
    arrayOfDecryptedBytes = createDecryptedByteArray(arrayOfEncryptedBytes, sharedKey, initialisation)   

    # get the clear text
    decryptedMessage = ""
    for decByte in arrayOfDecryptedBytes:
        decryptedMessage += chr(decByte)

    print("Decrypted message of " + byteArrayToString(arrayOfEncryptedBytes) + " that is delivered to User " + receiverUser + " : " + decryptedMessage)
    
main()