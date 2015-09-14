__author__ = 'Eric Owusu Sekyere'

"""
This is a console application  to demonstrate the caesar cipher.
This module allows for file input an output.
A User can test and experiment the caesar cipher either by encrypting some
input data or decrypting it
More on what the caesar cipher is and what it does here

https://en.wikipedia.org/wiki/Caesar_cipher

"""
import os
import time

MAX_KEY_SIZE = 26
write_decision = ""



def __introduce___():
    """
        An introductory Messsage
    """
    print("\t\t\t|--------------------------------------|")
    print("\t\t\t|          WELCOME TO THIS             |")
    print("\t\t\t|     SIMPLE CAESAR CIPHER MODULE      |")
    print("\t\t\t|--------------------------------------|")

def __invalid__():
    """
    To display when an input is invalid
    """
    print('\t\t\t      ****INVALID COMMAND****       ')



def prompt_user(message = ""):
    """
    To prompt the user for an input

    :param message: A message for the user
    :return: A prompt with the message provided
    """
    return input(message)


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
        time.sleep(0.5)
        print("\t\t\t|   encrypt(e) - to encrypt data       |")
        print("\t\t\t|               OR                     |")
        time.sleep(0.5)
        print("\t\t\t|   decrypt(d) - to decrypt data       |")
        print("\t\t\t|--------------------------------------|")
        mode = prompt_user(">> ").lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            __invalid__()

def get_key():

    """
    This method gets the user's preferred key {between 1 and 26 inclusive}
    The keys is used to encrypt or decrypt  a given input
    :return: the Key for encryption/ decrytion
    """
    key = 0
    while True:
        print("\t\t\t|--------------------------------------|")
        print('\t\t\t|      Enter the key number (1-%s)     |'
                            % (MAX_KEY_SIZE))
        print("\t\t\t|--------------------------------------|")
        key = prompt_user(">> ")
        #if(len(key)==0):
            #__invalid__()
        try:
            key = int(key)
            if (key >= 1 and key <= MAX_KEY_SIZE):
                return key
        except ValueError:
            __invalid__()


def getTranslatedMessage(mode, message, key):

    """
        This method will return the encrypted or decrypted message
        based on the mode, the given message and the cipher key

        :param mode(str): The mode, either encrypt or decrypt
        :param message(str): The message to decrypt or encrypt
        :param key(int): The key to encrypt of decrypt
        :return: The final message either decrypted or encrypted as string
    """
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            charnum = ord(symbol)
            charnum += key

            if symbol.isupper():
                if charnum > ord('Z'):
                    charnum -= 26
                elif charnum < ord('A'):
                    charnum += 26
            elif symbol.islower():
                if charnum > ord('z'):
                     charnum -= 26
                elif charnum < ord('a'):
                    charnum += 26

            translated += chr(charnum)
        else:
            translated += symbol
    return translated

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
        proceed_writing_file = prompt_user(">>  ")
        while(proceed_writing_file.lower() not in "yes y no n".split()):
            __invalid__()
            print("\t\t\t|--------------------------------------|")
            print("\t\t\t|       Proceed file writing?          |")
            print("\t\t\t|   Yes(y)       or           No(n)    |")
            print("\t\t\t|--------------------------------------|")
            proceed_writing_file = prompt_user(">>  ")
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
            print("\t\t\t|                     ||                    |")
            print("\t\t\t|---------------------||--------------------|")
            filename = prompt_user(">> ")
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
        print("\t\t\t|                     ||                    |")
        print("\t\t\t|---------------------||--------------------|")
        filename = prompt_user(">> ")+".txt"
        if(os.path.isfile(filename)):
            with open(filename, "r+") as textfile:
                return textfile.read()
        else:
            time.sleep(0.5)
            print("\t\t\t  ****The specified file does not exist****")




#=========================THE APPLICATION CODE BELOW==============================#
def app():

    mode, message, key = None, "",None

    __introduce___()

    while True:
        print("\t\t\t|--------------------------------------|")
        print("\t\t\t|       Would You Like to Proceed?     |")
        print("\t\t\t|   Yes(y)       or           No(n)    |")
        print("\t\t\t|--------------------------------------|")
        play = prompt_user(">> ")
        # user acceptance
        if(play.lower().startswith("y")):
            mode = action()
            #read from file or console
            print("\t\t\t|--------------------------------------|")
            print("\t\t\t|              ENTER(PUSH)             |")
            time.sleep(0.5)
            print("\t\t\t| f - to read from existing text file  |")
            print("\t\t\t|               OR                     |")
            time.sleep(0.5)
            print("\t\t\t| c -  read from console input         |")
            print("\t\t\t|--------------------------------------|")
            read_from_file = prompt_user(" ")
            #ensure user  puts in right command
            while(read_from_file.lower() not in "f c".split()):
                __invalid__()
                print("\t\t\t|--------------------------------------|")
                print("\t\t\t|              ENTER(PUSH)             |")
                time.sleep(0.5)
                print("\t\t\t| f - to read from existing text file  |")
                print("\t\t\t|               OR                     |")
                time.sleep(0.5)
                print("\t\t\t| c -  read from console input         |")
                print("\t\t\t|--------------------------------------|")
                read_from_file = prompt_user(">> ")
            else:
                # user decides to read from file
                if(read_from_file.lower()[0] is "f"):
                    message = read_file()
                else:
                    if(mode == "d" or mode == "decrypt"):
                        print("\t\t\t|--------------------------------------|")
                        print("\t\t\t|    Enter the message to decrypt      |")
                        print("\t\t\t|--------------------------------------|")
                    else:
                        print("\t\t\t|--------------------------------------|")
                        print("\t\t\t|    Enter the message to encrypt      |")
                        print("\t\t\t|--------------------------------------|")

                    message = prompt_user(">> ")
            key = get_key()
            write_file(getTranslatedMessage(mode, message, key))

        elif (play.lower().startswith("n")):
            time.sleep(0.5)
            print("\t\t\t|--------------------------------------|")
            print("\t\t\t|          Session Terminated          |")
            print("\t\t\t|--------------------------------------|")
            break
        else:
            time.sleep(0.5)
            __invalid__()


if __name__ == "__main__":
    app()



