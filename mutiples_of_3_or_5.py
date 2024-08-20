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

def solution(num):

    # num = int(input("Enter a number to find the sum of all multiples of 3 & 5 below it:\n"))

    # if num != int():
    #     print("Error! That isn't correct! Please enter an integer next time.")

    sum_of = 0

    for x in range(1, num):
        # This will iterate over every number from one 
        # to the integer that was an input in the function
        if x % 3 == 0:
            sum_of += x
        elif x % 5 == 0:
            sum_of += x   
        # If an integer that is divided by 3 or 5 does not have a remainder
        # Then it is a multiple, so it will be added to the sum
        # If 'x' is a mulutiple of 3 and 5, it will only be added to the sum once
        # The reason being is because if it meets the first condition,
        # if x % 3 == 0, it will be added to the sum automatically.
        else:
            pass

    return sum_of


print(solution(16))


