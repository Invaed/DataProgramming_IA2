#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Sum the major diagonal in a matrix) Write a function that sums all the numbers of the
# major diagonal in an
# matrix of integers using the following header:
# def sumMajorDiagonal(m):
# The major diagonal is the diagonal that runs from the top left corner to the bottom
# right corner in the square matrix. Write a test program that reads a matrix and
# displays the sum of all its elements on the major diagonal.
##############################################


def sumMajorDiagonal(m):
    total = 0
    for row in range(0, len(m)):
        for col in range(0, len(m[row])):
            if row == col:
                total += int(m[row][col])
    return total


# read matrix
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix = []
print("Enter the 4x4 matrix values below:")
for row in range(0, 4):
    matrix.append([])
    for col in range(0, 4):
        matrix[row].append(int(input()))
print(matrix)
print("Sum of major diagonal is:", sumMajorDiagonal(matrix))
