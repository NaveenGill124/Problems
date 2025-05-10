#--------------------a solution that only works in small inputs with time complexity O(N^2)------------------

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):

                if nums[i] == nums[j]:
                    return nums[i]
                    break


#---------------------------Here is the optimal solution---------------------------

