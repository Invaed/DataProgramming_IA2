#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Count the letters in a string) Write a function that counts the number of letters in a
# string using the following header:def countLetters(s):
# Write a test program that prompts the user to enter a string and displays the number
# of letters in the string.
##############################################


def countLetters(s):
    count = 0
    for i in range(0, len(s)):
        if s[i].isalpha():
            count += 1
    return count


input_string = input("Enter a string: ")
print("Number of letters is:", countLetters(input_string))
