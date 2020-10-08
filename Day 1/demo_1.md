Let's come up with a plan for the following problem...
```
We'll say that a positive int divides itself if every digit in the number divides into the number evenly. So for example 128 divides itself since 1, 2, and 8 all divide into 128 evenly.

And we'll say that 0 does not divide into anything evenly, so no number with a 0 digit divides itself.

Write a function to determine if a number divides itself.

[source - https://codingbat.com/prob/p165941]
```

**Understand**
1. How do we check each digit of a number?
2. How can we move from one digit to the next?
3. How do we know check if the digit divides the number without a remainder?
4. How do we store each digit as we go through the division?

- should we deal with non numeric values? -> leave up to engineer
- how should we handle decimal values? -> we should only take in an int
- what should this function return? True or False?


**Plan**
1. create a function that takes in an int (not a float)
2. store that int as a string.
3. take slices of that and turn it back into a number
4. divide that int(slice) by the whole number
5. check if that int(slice) divides evenly into the number (without a remainder)
6. stop when the int(slice) does not evenly go into the whole number
7. Then return True or False depending on if all the digits divide the number evenly

# loop through digits in the number
# - use % to get the rightmost digit
# - use / to discard the rightmost digit
# - if dividing by the single digit leaves a remainder, return False
# - if the digit is a 0 also return False

# - if the loop exits without returning False, then return True