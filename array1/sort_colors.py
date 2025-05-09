class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        nums.sort()
# ----------------------------- build in function which takes O(nlogn) time complexity --------------------------
class Solution:
    def sortColors(self, nums: List[int]) -> None:
                
        x, y, z = 0, 0, 0

        for num in nums:
            
            if num == 0:
                x = x + 1
            elif num == 1:
                y = y + 1
            elif num == 2:
                z = z + 1
            
        for i in range(0, x):
            nums[i] = 0

        for i in range(x, x+y):
            nums[i] = 1
        
        for i in range(x+y, x+y+z):
            nums[i] = 2

# ----------------------------- slightly better approach --------------------------

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        n = len(nums)
        mid,  low = 0, 0
        high = n-1
        while (mid <= high):

            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low = low + 1
                mid = mid + 1
            
            elif nums[mid] == 1:
                mid = mid + 1
            
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high = high - 1

              
# Time Complexity: O(n) 
# Space Complexity: O(1) 
