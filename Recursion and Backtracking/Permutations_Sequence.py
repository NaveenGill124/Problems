class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        def fact(n):
            fact = 1
            for i in range(2, n+1):

                fact *= i
            
            return fact
        
        nums = [str(i) for i in range(1, n + 1)]
        k = k-1 # Convert to 0-based index

        result = []

        for i in range(n):
            f = fact(n - 1 - i)
            idx = k // f
            result.append(nums.pop(idx))
            k %= f

        return ''.join(result)
