class Solution:
    
    def search(self, nums: List[int], target: int) -> int:

        high = len(nums) - 1
        low = 0
            
        while low <= high:

            mid = (low+high)//2

            if nums[mid] == target:
                return mid
            
            if nums[low] <= nums[mid]:

                if nums[low] <= target <= nums[mid-1]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            else:
                if nums[mid+1] <= target <= high:
                    low = mid + 1
                else:
                    high = mid -1
        
        return -1
