#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Sort students) Write a program that prompts the user to enter the students’ names and
# their scores on one line and prints student names in increasing order of their scores.
# (Hint: Create a list. Each element in the list is a sublist with two elements: score and
# name. Apply the sort method to sort the list. This will sort the list on scores.)
##############################################

student_count = int(input("Enter total number of student's: "))
student_lst = []
for i in range(0, student_count):
    student_name, student_score = input("Enter student" + str(i) + " name and scores on one line: ").split(" ")
    student_lst.append([student_name, int(student_score)])
student_lst.sort(key=lambda x: x[1])
print(student_lst)