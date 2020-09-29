def main():
    playfair()


def playfair():
    modeType = ""
    mode = input("Would you like to:\n\t(1) encrypt\n\t(2) decrypt\n")
    if(mode == "1"):
        modeType = "encrypt"
    elif(mode == "2"):
        modeType = "decrypt"
    key = input("Please enter a key: ")
    message = input("Please enter a message to " + modeType + ": ")
    print(f"\nSYS: PROCESS STARTED USING {modeType}")
    if(mode == "1"):
        encrypt(key.upper(), message.upper())
    elif(mode == "2"):
        decrypt(key.upper(), message.upper())
    else:
        print("\nERR: Please enter a valid mode.")


def matrix(key):
    # Removes duplicates and adds key characters,
    # followed by the remaining letters
    line = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTVWXYZ"
    pos = 0
    for char in key:
        if(char not in line):
            line.append(char)
    while(pos < 25):
        if(alphabet[pos] not in line):
            line.append(alphabet[pos])
        pos += 1
    print("\nSYS: MATRIX GENERATED")
    return line


def removeSpecials(message):
    # Removes U and Q from the alphabet
    fmessage = ""
    for char in message:
        if(char == "U"):
            fmessage += "V"
        elif(char == "Q"):
            fmessage += "K"
        else:
            fmessage += char
    return fmessage


def removeSpaces(message):
    # Removes spaces and assigns them to Q
    fmessage = ""
    for char in message:
        if(char == " "):
            fmessage += "Q"
        else:
            fmessage += char
    return fmessage


def addSpaces(message):
    fmessage = ""
    for char in message:
        if(char == "Q"):
            fmessage += " "
        else:
            fmessage += char
    return fmessage


def formatMessage(message):
    # Separates the message into pairs
    messageList = []
    pos = 0
    if len(message) % 2 == 0:
        while pos < len(message):
            messageList.append(message[pos] + message[pos + 1])
            pos += 2
    else:
        while pos < len(message) - 1:
            messageList.append(message[pos] + message[pos + 1])
            pos += 2
        messageList.append(message[pos] + "Q")
    return messageList


def removeDoubles(messageList):
    # Removes duplicate letters changing the second letter to X if a duplicate
    fmessageList = []
    for pos in range(len(messageList)):
        if(messageList[pos][0] == messageList[pos][1]):
            fmessageList.append(messageList[pos][0] + "X")
        else:
            fmessageList.append(messageList[pos])
    return fmessageList


def addDoubles(message):
    fmessage = ""
    for pos in range(len(message)):
        if(message[pos] == "X"):
            fmessage += message[pos - 1]
        else:
            fmessage += message[pos]
    return fmessage


def checkRow(fmessage, line, pos):
    # Checks to see if any pairs are contained in the same row
    lPos = 0
    rPos = [20, 21, 22, 23, 24]
    x = 0
    # Finds the position of the charcter from the message on the matrix
    for pos2 in range(len(line)):
        if fmessage[pos][0] == line[pos2]:
            lPos = pos2
    # Determins the row of the character based on position
    if(lPos < 5):
        rPos = [0, 1, 2, 3, 4]
    elif((lPos < 10) & (lPos > 4)):
        rPos = [5, 6, 7, 8, 9]
    elif((lPos < 15) & (lPos > 9)):
        rPos = [10, 11, 12, 13, 14]
    elif((lPos < 20) & (lPos > 14)):
        rPos = [15, 16, 17, 18, 19]
    # Checks the positions on the row of interest for duplicates
    for x in range(5):
        if line[rPos[x]] == fmessage[pos][1]:
            return True
    return False


def checkCollumn(fmessage, line, pos):
    # lPos = position in line[]
    lPos = 0
    cPos = [4, 9, 14, 19, 24]
    x = 0
    for pos2 in range(len(line)):
        if fmessage[pos][0] == line[pos2]:
            lPos = pos2
    if(lPos % 5 == 0):
        cPos = [0, 5, 10, 15, 20]
    elif((lPos - 1) % 5 == 0):
        cPos = [1, 6, 11, 16, 21]
    elif((lPos - 2) % 5 == 0):
        cPos = [2, 7, 12, 17, 22]
    elif((lPos - 3) % 5 == 0):
        cPos = [3, 8, 13, 18, 23]
    for x in range(5):
        if line[cPos[x]] == fmessage[pos][1]:
            return True
    return False


def encryptRow(pair, line):
    # Encrypts pairs of characters that share the same row
    encryptedPair = ""
    for x in range(25):
        if line[x] == pair[0]:
            # If the character is at the end of the row,
            # assign it to the character at the first position of the row
            if (x+1) % 5 == 0:
                encryptedPair += line[x-4]
            else:
                encryptedPair += line[x+1]
    for x in range(25):
        if line[x] == pair[1]:
            if (x+1) % 5 == 0:
                encryptedPair += line[x-4]
            else:
                encryptedPair += line[x+1]
    return encryptedPair


def encryptCollumn(pair, line):
    # Encrypts pairs of characters that share the same collumn
    encryptedPair = ""
    for x in range(25):
        if line[x] == pair[0]:
            if((4 - (24-x)) < 0):
                encryptedPair += line[x+5]
            else:
                encryptedPair += line[4 - (24-x)]
    for x in range(25):
        if line[x] == pair[1]:
            if((4 - (24-x)) < 0):
                encryptedPair += line[x+5]
            else:
                encryptedPair += line[4 - (24-x)]
    return encryptedPair


def encryptCorners(pair, line):
    cPos = 4
    cPos2 = 4
    lPos = 0
    lPos2 = 0
    encryptedPair = ""
    # Finds the collumn and position of the character
    for x in range(25):
        if line[x] == pair[0]:
            if(x % 5 == 0):
                cPos = 0
            elif((x - 1) % 5 == 0):
                cPos = 1
            elif((x - 2) % 5 == 0):
                cPos = 2
            elif((x - 3) % 5 == 0):
                cPos = 3
            lPos = x
    for x in range(25):
        if line[x] == pair[1]:
            if(x % 5 == 0):
                cPos2 = 0
            elif((x - 1) % 5 == 0):
                cPos2 = 1
            elif((x - 2) % 5 == 0):
                cPos2 = 2
            elif((x - 3) % 5 == 0):
                cPos2 = 3
            lPos2 = x
    # Finds the appropriate encrypted pairs
    # based on the difference of their collumn positions
    if(lPos2 < lPos):
        lPos += (cPos2 - cPos)
        encryptedPair += line[lPos]
    elif(lPos2 > lPos):
        lPos -= (cPos - cPos2)
        encryptedPair += line[lPos]
    if(lPos2 < lPos):
        lPos2 -= (cPos2 - cPos)
        encryptedPair += line[lPos2]
    elif(lPos2 > lPos):
        lPos2 += (cPos - cPos2)
        encryptedPair += line[lPos2]
    return encryptedPair


def decryptRow(pair, line):
    decryptedPair = ""
    for x in range(25):
        if line[x] == pair[0]:
            if x % 5 == 0:
                decryptedPair += line[x+4]
            else:
                decryptedPair += line[x-1]
    for x in range(25):
        if line[x] == pair[1]:
            if x % 5 == 0:
                decryptedPair += line[x+4]
            else:
                decryptedPair += line[x-1]
    return decryptedPair


def decryptCollumn(pair, line):
    decryptedPair = ""
    for x in range(25):
        if line[x] == pair[0]:
            if((x-5) > 0):
                decryptedPair += line[x-5]
            else:
                decryptedPair += line[x+20]
    for x in range(25):
        if line[x] == pair[1]:
            if((x-5) > 0):
                decryptedPair += line[x-5]
            else:
                decryptedPair += line[x+20]
    return decryptedPair


def encrypt(key, message):
    line = matrix(key)
    formattedMessage = removeDoubles(
        formatMessage(removeSpaces(removeSpecials(message))))
    print("\nSYS: ENCRYPTED PAIRS GENERATED")
    print("Encrypting...")
    encryptedMessage = ""
    for pos in range(len(formattedMessage)):
        if checkRow(formattedMessage, line, pos):
            encryptedPair = encryptRow(formattedMessage[pos], line)
            encryptedMessage += encryptedPair
        elif checkCollumn(formattedMessage, line, pos):
            encryptedPair = encryptCollumn(formattedMessage[pos], line)
            encryptedMessage += encryptedPair
        else:
            encryptedPair = encryptCorners(formattedMessage[pos], line)
            encryptedMessage += encryptedPair
    print("""\nSYS: PROCESS COMPLETED\n
        \nNote: Spaces have been assigned character 'Q'""")
    print(f"\nEncrypted Message: {encryptedMessage}\n")


def decrypt(key, message):
    line = matrix(key)
    formattedMessage = formatMessage(message)
    decryptedMessage = ""
    print("\nSYS: DECRYPTED PAIRS GENERATED")
    print("Decrypting...")
    for pos in range(len(formattedMessage)):
        if checkRow(formattedMessage, line, pos):
            decryptedPair = decryptRow(formattedMessage[pos], line)
            decryptedMessage += decryptedPair
        elif checkCollumn(formattedMessage, line, pos):
            decryptedPair = decryptCollumn(formattedMessage[pos], line)
            decryptedMessage += decryptedPair
        else:
            decryptedPair = encryptCorners(formattedMessage[pos], line)
            decryptedMessage += decryptedPair
    fDecryptedMessage = addSpaces(addDoubles(decryptedMessage))
    print("\nSYS: PROCESS COMPLETED")
    print(f"\nDecrypted Message: {fDecryptedMessage}")


main()
