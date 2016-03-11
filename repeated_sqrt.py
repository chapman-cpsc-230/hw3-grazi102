    ```
    """
    File: repeated_sqrt.py

    Copyright (c) 2016 Lauren Graziani

    License: MIT

    <Explaining how a program works. Excercise 2.18 in book.
    """
    ```




from math import sqrt
for n in range(1, 60): #calculates number of times to  take square root
    r = 2.0 # variable r = 2.0
    for i in range(n):
        r = sqrt(r) # taking the square root of variable r changing r  to that #
    for i in range (n):
        r = r**2 #squares r. Which then return it back to the same number
    print "%d times sqrt and **2: %.16f " % (n, r)

"""
1 squared any number of times is still 1 so the second operation leaves the number the same and 2 is not recovered
"""
