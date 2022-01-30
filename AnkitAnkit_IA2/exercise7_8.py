#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Find the index of the smallest element) Write a function that returns the index of the
# smallest element in a list of integers. If the number of such elements is greater than 1,
# return the smallest index. Use the following header:
# def indexOfSmallestElement(lst):
# Write a test program that prompts the user to enter a list of numbers in one line,
# invokes this function to return the index of the smallest element, and displays the
# index.
##############################################


def indexOfSmallestElement(lst):
    return lst.index(min(lst))


number_lst = input("Enter the list of numbers in one line: ").split(" ")
print("Index of smallest number is:",indexOfSmallestElement(number_lst))