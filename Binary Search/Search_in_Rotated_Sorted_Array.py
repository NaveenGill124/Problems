class Solution:
    
    def search(self, nums: List[int], target: int) -> int:

        high = len(nums) - 1
        low = 0
            
        while low <= high:

            mid = (low+high)//2

            if nums[mid] == target:
                return mid
            
            if nums[low] <= nums[mid]:

                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid -1
        
        return -1

        
