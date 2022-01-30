#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Sorted?) Write the following function that returns true if the list is already sorted in
# increasing order:
# def isSorted(lst):
# Write a test program that prompts the user to enter a list of numbers in one line and
# displays whether the list is sorted or not.
##############################################


def isSorted(lst):
    if sorted(lst) == lst:
        return True
    return False


input_list = input("Enter a list of numbers in one line: ").split(" ")
if isSorted(input_list):
    print("The list is sorted")
else:
    print("The list is not sorted")
