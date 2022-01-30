#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Sum elements column by column) Write a function that returns the sum of all the
# elements in a specified column in a matrix using the following header:
# def sumColumn(m, columnIndex):
# Write a test program that reads a matrix and displays the sum of each column.
##############################################


def sumColumn(m, columnIndex):
    total = 0
    for row in range(0, len(matrix)):
        total += int(matrix[row][columnIndex])
    return total


# read matrix
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matrix = []
print("Enter the 3x4 matrix values below:")
for row in range(0, 3):
    matrix.append([])
    for col in range(0, 4):
        matrix[row].append(int(input()))
# print(matrix)

# print sum of each column
for i in range(0, len(matrix[0])):
    print("Sum of column", i, "is:", sumColumn(matrix, i))
