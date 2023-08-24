# ------------------------------------------------- #
# Title: Assignment 07 Pickling
# Description: Snippets of code to demonstrate exception handling
# https://www.programiz.com/python-programming/exceptions
# ChangeLog: (Who, When, What)
# PChuoy,<8.23.2023>,Copied code
# ------------------------------------------------- #

# ------------------------------------------------- #
# Try-Except block example
try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

# Output: Error: Denominator cannot be 0.
# ------------------------------------------------- #

# ------------------------------------------------- #
# Example of catching specific exceptions
try:

    even_numbers = [2, 4, 6, 8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")

except IndexError:
    print("Index Out of Bound.")

# Output: Index Out of Bound
# ------------------------------------------------- #

# ------------------------------------------------- #
# Try with Else Clause
# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
# ------------------------------------------------- #

# ------------------------------------------------- #
# Try finally
try:
    numerator = 10
    denominator = 0

    result = numerator / denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

finally:
    print("This is finally block.")
# ------------------------------------------------- #