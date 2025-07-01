class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1
        while low <high:

            mid = (low + high) // 2

            if mid == 0:
                if nums[mid] != nums[mid + 1]:
                    return nums[mid]
            elif mid == len(nums) - 1:
                if nums[mid] != nums[mid - 1]:
                    return nums[mid]
            else:
                if nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
                    return nums[mid]

            if mid%2 == 0:

                if nums[mid] == nums[mid-1]:
                    
                    
                    high = mid -1
                else:
                    low = mid + 1
                    
                    
            
            else:
                if nums[mid] == nums[mid-1]:
                    
                    low = mid + 1
                else:
                    high = mid -1

        return nums[low] 
