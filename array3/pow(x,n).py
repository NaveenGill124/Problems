class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        return x**n

#--------------------------One line answer with time complexity O(logn)---------------

#--------------------------------but for manually doing this--------------------------

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def fast_pow(x, n):
            if n == 0:
                return 1
            half = fast_pow(x, n // 2) # recursive call

            return half * half if n % 2 == 0 else half * half * x
        
        result = fast_pow(x, abs(n))
        return result if n >= 0 else 1 / result
        
            # recursive call
            '''
            fast_pow(2, 5)
            └── fast_pow(2, 2)
                └── fast_pow(2, 1)
                    └── fast_pow(2, 0) → 1
                    → returns 2
                → returns 4
            → returns 32
            '''
