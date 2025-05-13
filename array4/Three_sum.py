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

