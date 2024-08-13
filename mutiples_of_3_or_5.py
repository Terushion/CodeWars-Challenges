# multples_3_or_5.py

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.

expected output if input = 20:

output = sum of 3, 5, 6, 9, 10, 12, 15, 18
output = 78

"""

def solution():

    num = int(input("Enter a number to find the sum of all multiples of 3 & 5 below it:\n"))

    # if num != int():
    #     print("Error! That isn't correct! Please enter an integer next time.")

    sum_of = 0

    if num < 0:
        return 0
    else:
        for x in range(0, num - 1):
            if x % 3 or 5 == 0:
                sum_of += x
            else:
                pass
    
    return sum_of


print(solution())


