#############################################
#####  Ankit || ankit02@student.gsu.edu #####
#############################################
# (Financial application: compute commissions) Write a function that computes the
# commission, using the scheme in Programming Exercise 5.39 . The header of the
# function is as follows:def computeCommission(salesAmount):
# Write a test program that displays the following table:
##############################################


def computeCommission(salesAmount):
    commission = 0
    if 0.01 <= salesAmount <= 5000:
        commission = salesAmount * 0.08
    elif 5000.01 <= salesAmount <= 10000:
        commission = (5000 * 0.08) + ((salesAmount-5000) * 0.1)
    elif salesAmount >= 10000.01:
        commission = (5000 * 0.08) + (5000 * 0.10) + ((salesAmount - 10000) * 0.12)
    return commission


print("Sales amount \t Commission")
for i in range(10000, 100001, 5000):
    print(i, "\t", str(round(computeCommission(i), 1)).rjust(18))
