# Simple Transposition Cipher Encryption/Decryption
# More from Inventwithpython.com
import os
import time
import math

def invalid():
    print("\t\t\t\t *****Invalid Command*****")

def __proceed__():
    print("\t\t\t|--------------------------------------|")
    print("\t\t\t|       Would You Like to Proceed?     |")
    print("\t\t\t|   Yes(y)       or           No(n)    |")
    print("\t\t\t|--------------------------------------|")

def action():

    """
    The function  request to the user to provide a mode
    when the method is called the user will be prompted to select  one of two modes
    to decrypt or encrypt
    :return: the mode which the user has chosen
    """
    while True:
        print("\t\t\t|--------------------------------------|")
        print("\t\t\t|             ENTER(PUSH)              |")
        time.sleep(0.2)
        print("\t\t\t|   encrypt(e) - to encrypt data       |")
        print("\t\t\t|               OR                     |")
        time.sleep(0.2)
        print("\t\t\t|   decrypt(d) - to decrypt data       |")
        print("\t\t\t|--------------------------------------|")
        mode = input(">> ").lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            invalid()

def read_file():

    """
    This function allows the the user  allow the user to specify file to read from
    When the method is called the user is prompted to enter a file to read from

    :return:The contents of the user specified file
    """
    while True:
        time.sleep(0.5)
        print("\t\t\t|-------------------------------------------|")
        print("\t\t\t| Enter an existing file to read from below |")
        print("\t\t\t|-------------------------------------------|")
        filename = input(">> ")+".txt"
        if(os.path.isfile(filename)):
            with open(filename, "r+") as textfile:
                return textfile.read()
        else:
            print("\t\t\t  ****The specified file does not exist****")

def write_file(text = ""):

    """
    This method allows for file writing  data to a given the file
    when this method is called the user will be prompted to with a choice of writing to file
    or  not . should the user choose to write to file
    the user will be prompted to provide a file name
    if no file name is provided a default name "file" is assigned.
    The input text is written to the file

    :param text: the text to write to the input file
    :return: True if user decides to proceed with file writing
    """
    while(True):
        print("\t\t\t|--------------------------------------|")
        print("\t\t\t|       Proceed file writing?          |")
        print("\t\t\t|   Yes(y)       or           No(n)    |")
        print("\t\t\t|--------------------------------------|")
        proceed_writing_file = input(">>  ")
        while(proceed_writing_file.lower() not in "yes y no n".split()):
            invalid()
            print("\t\t\t|--------------------------------------|")
            print("\t\t\t|       Proceed file writing?          |")
            print("\t\t\t|   Yes(y)       or           No(n)    |")
            print("\t\t\t|--------------------------------------|")
            proceed_writing_file = input(">>  ")
        if(proceed_writing_file.startswith("n")):
            print("\t\t\t|--------------------------------------|")
            print("\t\t\t|  The translated message is below     |")
            print("\t\t\t|--------------------------------------|")
            time.sleep(1)
            print(text)
            return False
        else:
            print("\t\t\t|-------------------------------------------|")
            print("\t\t\t|      Enter a  file to write to below      |")
            print("\t\t\t|-------------------------------------------|")
            filename = input(">> ")
            if(len(filename) == 0):
                filename = "file"
            filename+=".txt"
            with open(filename,'w') as textfile:
                textfile.write(text)
                time.sleep(1)
                print("\t\t\t|------------------------------------------------|")
                print("\t\t\t|   Content has been written to the file named %s|"%(filename))
                print("\t\t\t|------------------------------------------------|")
               # print("Content has been written to the file"+ filename)
                break
    return True



def get_key():
    key = 0
    while (True):
        print("\t\t\t|--------------------------------------|")
        print("\t\t\t|         Enter the key number         |")
        print("\t\t\t|--------------------------------------|")
        key = input(">> ")
        try:
            key = int(key)
            return key
        except ValueError:
            invalid()

def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key

    # Loop through each column in ciphertext.
    for col in range(key):
        pointer = col

        # Keep looping until pointer goes past the length of the message.
        while pointer < len(message):
            # Place the character at pointer in message at the end of the
            # current column in the ciphertext list.
            ciphertext[col] += message[pointer]

            # move pointer over
            pointer += key

    # Convert the ciphertext list into a single string value and return it.
    return ''.join(ciphertext)

def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    numOfColumns = math.ceil(len(message) / key)
    # The number of "rows" in our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * numOfColumns

    # The col and row variables point to where in the grid the next
    # character in the encrypted message will go.
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1 # point to next column

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row.
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)

def app():
    message, key, mode,translated, choice = "", None, "", "", ""
    print ("\t\t\t|--------------------------------------|")
    print ("\t\t\t|        welcome to this simple        |".upper())
    print ("\t\t\t|         transposition Ciphers         |".upper())
    print ("\t\t\t|--------------------------------------|")
    
    while(True):
        # user decision
        __proceed__()
        proceed = input(">> ").lower()
        
        if(proceed in "y yes".split()):
                mode = action()
                print("Would you like to use the console or read from file")
                choice = input('>> ').lower()
                while(choice not in "r c console read".split()):
                    invalid()
                    print("Would you like to use the console or read from file")
                    choice = input('>> ')
                else:
                    if choice in "r read".split():
                        print("Enter the file to read from")
                        message = read_file()
                    else:
                        print("Enter the message below")
                        message = input(">> ")
                # got message at this point
                #now get the key
                key = get_key()
                if((mode == "e" or mode == "encrypt")):
                    translated = encryptMessage(key, message) + "|"
                elif ((mode == "d" or mode == "decrypt")):
                    translated = encryptMessage(key, message) + "|"
                write_file(translated)

        elif(proceed in "n no".split()):
            time.sleep(0.5)
            print("\t\t\t|--------------------------------------|")
            print("\t\t\t|          Session Terminated          |")
            print("\t\t\t|--------------------------------------|")            
            break
        else:
            invalid()
            __proceed__()


    myMessage = 'Common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen, with
    # a | (called "pipe" character) after it in case there are spaces at
    # the end of the encrypted message.
    print(ciphertext + '|')

    # Copy the encrypted string in ciphertext to the clipboard.


# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    app()