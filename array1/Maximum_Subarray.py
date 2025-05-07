class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf') # Initialize to lowest possible value
        current_sum = 0

        for i in nums:

            current_sum += i

            if current_sum > maxSum:
                maxSum = current_sum
            
            if current_sum < 0:
                current_sum = 0
        
        return maxSum
            
