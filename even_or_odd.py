# even_or_odd.py

"""
Create a function that takes an integer as an argument and,
returns "Even" for even numbers or "Odd" for odd numbers

"""

def even_or_odd(number):

    # Check if input is not an integer
    if not isinstance(number, int):
        return 'Null'

    # Checks if the number is not a multiple of 2
    if (number % 2) != 0:
        return 'Odd'
    # If dividable by 2, then it is an even number
    else:
        return 'Even'
     
print(even_or_odd(8))  # Expected outcome: 'Even'
print(even_or_odd(3))  # Expected outcome: 'Odd'
print(even_or_odd('s'))  # Expected outcome: 'Null'
print(even_or_odd(0))  # Expected outcome: 'Even'