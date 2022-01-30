#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Eliminate duplicates) Write a function that returns a new list by eliminating the
# duplicate values in the list. Use the following function header:
# def eliminateDuplicates(lst):
# Write a test program that reads in a list of integers in one line, invokes the function,
# and displays the result.
##############################################


def eliminateDuplicates(lst):
    return list(set(lst))


input_list = input("Enter all the integers in 1 line: ").split(" ")
print("Output without duplicates:", eliminateDuplicates(input_list))
