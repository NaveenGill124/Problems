#-------------------------------first solutiin with O(n^2)---------------------------------------
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
            
#----------------------here is the solution for time complexity O(n)-----------
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}

        for i in range(len(nums)):

            num = nums[i]

            comp = target - num # complement of the current number

            if comp in dic:
                return [dic[comp], i]
                
            dic[num] = i
