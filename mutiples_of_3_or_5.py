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

    sum_of = 0
    
    # num = int(input("Enter a number to find the sum of all multiples of 3 & 5 below it:\n"))

    # if num != int():
    #     print("Error! That isn't correct! Please enter an integer next time.")

    if num < 0:
        return 0

    for x in range(1, num):
        # This will iterate over every number from one 
        # to the integer that was an input in the function
        if x % 3 == 0:
            sum_of += x
        # Check if the number is a multiple of 5, but not already added
        elif x % 5 == 0:
            sum_of += x   
        else:
            # If an integer that is divided by 3 or 5 DOES have a remainder
            # Then it is not a multiple, and therefore the loop will pass onto the next            # 
            pass

    return sum_of

print(solution(16)) # Expected output: 60
print(solution(-1)) # Expected output: 0


