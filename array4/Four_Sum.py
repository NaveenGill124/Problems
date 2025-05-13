#------------------brute-force approach----------------

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):

                        res = nums[i] + nums[j]+ nums[k] + nums[l]

                        if res == target and (nums[i] , nums[j] , nums[k] , nums[l]) not in result:
                            result.append([nums[i] , nums[j] , nums[k] , nums[l]])

        return result

#----------------------------Here is the optimal solution--------------------


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        pre_set = set()
        n = len(nums)
        result = []
        nums.sort()
        for i in range(n):

            if i>0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, n):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                p, q = j+1 , n-1
                while p<q:
                    s = nums[p]+nums[q]+nums[i]+ nums[j]
                    if s ==target:

                        quad = [nums[p],nums[q],nums[i],nums[j]]
                        
                        result.append(quad)

                        p = p+1
                        q = q-1

                        while(p<q and nums[p] == nums[p-1]):
                            p = p+1
                        
                        while(q>p and nums[q] == nums[q+1]):
                            q = q-1
                            
                    
                    if s < target:
                        p = p+1
                    if  s > target:

                        q = q-1
                    
        return result






