class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count = 0
        max_count = 0
        for i in range(len(nums)):

            if nums[i] == 1:
                count += 1
                max_count = max(max_count, count) # in the first place I forgot the max function to use, later realise that we can use max function to solve this

            else:
                count = 0
        
        return max_count

  
