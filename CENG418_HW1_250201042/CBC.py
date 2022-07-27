# the function the xOR process for given byte with sharedKey and initialisation value (IV or C,M)
def doXOR(initialisation, byte, sharedKey):
    return byte ^ sharedKey ^ initialisation

