"""
We'll say that a positive int divides itself if every digit in the number divides into the number evenly.
So for example 128 divides itself since 1, 2, and 8 all divide into 128 evenly.
And we'll say that 0 does not divide into anything evenly, so no number with a 0 digit divides itself.
Write a function to determine if a number divides itself.

[source - https://codingbat.com/prob/p165941]
"""

# loop through digits in the number
# - use % to get the rightmost digit
# - use / to discard the rightmost digit
# - if dividing by the single digit leaves a remainder, return False
# - if the digit is a 0 also return False

# - if the loop exits without returning False, then return True

def divide_self(num):
    # set a temp variable to hold the number
    value = int(num)
    # loop over the digits in the number
    # while the value is not zero
    while value != 0:
        # extract the single digit by moddling the value by 10
        digit = int(value % 10)
        # print(digit)
        # check if the digit is zero or if the num mod the digit is not zero
        if digit == 0 or num % digit != 0:
            # return False
            return False

        # divide our value by 10 to make sure we do not get an infinite loop
        value = value//10

    # return True
    return True

# my solution was used in class solution!!!
def divide_self1(num):
    val_list = [int(x) for x in str(num)]
    for val in val_list:
        if val == 0 or num % val != 0:
            return False
    return True

print(divide_self(128))
print(divide_self(12))
print(divide_self(120))

print(divide_self1(128))
print(divide_self1(12))
print(divide_self1(120))
