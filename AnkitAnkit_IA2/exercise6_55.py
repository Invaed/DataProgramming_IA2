#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Phone keypads) The international standard letter/number mapping for telephones is:
# Write a function that returns a number, given an uppercase letter, as follows:
# def getNumber(uppercaseLetter):
# Write a test program that prompts the user to enter a phone number as a string. The
# input number may contain letters. The program translates a letter (uppercase or
# lowercase) to a digit and leaves all other characters intact.
##############################################


def getNumber(uppercaseLetter):
    letter_number_mapping = {'a': 2, 'b': 2, 'c': 2,
                             'd': 3, 'e': 3, 'f': 3,
                             'g': 4, 'h': 4, 'i': 4,
                             'j': 5, 'k': 5, 'l': 5,
                             'm': 6, 'n': 6, 'o': 6,
                             'p': 7, 'q': 7, 'r': 7, 's': 7,
                             't': 8, 'u': 8, 'v': 8,
                             'w': 9, 'x': 9, 'y': 9, 'z': 9}
    return letter_number_mapping[uppercaseLetter.lower()]


input_string = input("Enter a phone number as a string: ")
translation = " "
for i in range(0, len(input_string)):
    # print(input_string[i])
    if input_string[i].isalpha():
        translation = str(translation) + str(getNumber(input_string[i]))
    else:
        translation = translation + str(input_string[i])
print("Phone keypad translation:", translation)