#---------------------with time complexity O(n^3 * log(unique triplets)) and space complexity will be ---------------------- O(unique triplets)-------

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pre_set = set()
        n = len(nums)
        target = 0
        result = []
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    res = nums[i] + nums[j]+ nums[k]

                    tri = tuple(sorted((nums[i] , nums[j], nums[k])))

                    if res == target:

                        if tri not in pre_set:
                            pre_set.add(tri)
                            result.append(list(tri))
            
        
        return result
#--------------------not a right solution---------------




