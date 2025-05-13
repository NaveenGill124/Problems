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
#--------------------not a right solution---------------O(n^2)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pre_set = set()
        n = len(nums)
        target = 0
        result = []
        nums.sort()
        for i in range(n-2):

            if i>0 and nums[i] == nums[i-1]:
                continue
            
            seen = set()
            for j in range(i+1, n):
                
                comp = -nums[i] - nums[j]

                if comp in seen:

                    trip = (nums[i], nums[j], comp)

                    if trip not in pre_set:
                        pre_set.add(trip)
                        result.append(list(trip))
                
                seen.add(nums[j])         
        
        return result



