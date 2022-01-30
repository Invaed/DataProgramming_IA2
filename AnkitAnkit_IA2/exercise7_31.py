#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Occurrences of each digit in a string) Write a function that counts the occurrences of
# each digit in a string using the following header:
# def count(s):
# The function counts how many times a digit appears in the string. The return value is a
# list of ten elements, each of which holds the count for a digit. For example, after
# executing counts = count("12203AB3") , counts[0] is 1 , counts[1] is
# 1 , counts[2] is 2 , and counts[3] is 2 .
# Write a test program that prompts the user to enter a string and displays the number
# of occurrences of each digit in the string.
##############################################


def count(s):
    counts = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]
    for i in range(0, len(s)):
        if s[i].isnumeric():
            counts[int(s[i])][1] = s.count(s[i])
    return counts


input_string = input("Enter the string: ")
counts = count(input_string)
for i in range(0, len(counts)):
    if counts[i][1] > 0:
        print("Counts[" + str(i) + "] is", counts[i][1])
