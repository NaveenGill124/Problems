# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
#You must not use any built-in exponent function or operator.
#For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
#Input: x = 4
#Output: 2
#Explanation: The square root of 4 is 2, so we return 2.

class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x
        
        low = 0
        high = x

        while low <= high:

            mid =( low+high)//2

            if mid*mid == x:
                return mid
            elif mid*mid < x:
                low = mid + 1
            else:
                high = mid -1
            
        
        return high # After loop, high is the integer part of sqrt(x)
