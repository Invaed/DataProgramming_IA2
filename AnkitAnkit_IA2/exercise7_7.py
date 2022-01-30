#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Count single digits) Write a program that generates 1,000 random integers between 0
# and 9 and displays the count for each number. (Hint: Use a list of ten integers, say
# counts , to store the counts for the number of 0s, 1s, …, 9s.)
##############################################
import random

random_numbers = [random.randint(0, 9) for x in range(0, 1000)]
counts = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]
for i in range(0, 10):
    counts[i][1]= random_numbers.count(i)
print(counts)