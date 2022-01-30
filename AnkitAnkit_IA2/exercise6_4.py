#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# Write a function with the following header to display an integer in reverse order:
# For example, reverse(3456) displays 6543 . Write a test program that prompts
# the user to enter an integer and displays its reversal.
##############################################


def reverse(number):
    reverse_number = str(number)
    return reverse_number[::-1]


print("Reverse is:", reverse(3456))
