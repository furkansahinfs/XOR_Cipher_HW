import random

 # A private value for given user is taken from user
def getUserPrivateValue(userName):
    privateValue = int(input("Enter the private value for User " + userName + " : "))
    return privateValue

# Get message of User
def getUserMessage(userName):
    message = input("Enter the message for User " + userName +": ")
    return message

def getByteArrayOfMessage(message):
    return bytearray(message,"utf-8")
