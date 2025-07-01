from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Initialize pointers for binary search
        low = 0
        high = len(nums) - 1

        # Binary search loop
        while low < high:
            mid = (low + high) // 2  # Get middle index

            # Edge case: if mid is at the beginning and is not equal to next
            if mid == 0:
                if nums[mid] != nums[mid + 1]:
                    return nums[mid]
            # Edge case: if mid is at the end and is not equal to previous
            elif mid == len(nums) - 1:
                if nums[mid] != nums[mid - 1]:
                    return nums[mid]
            # General case: if mid is not equal to neighbors, it's the single element
            else:
                if nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
                    return nums[mid]

            # Now we decide which half to continue searching based on the pattern

            # If mid is even and equals the previous element,
            # it means the single element is on the left half
            if mid % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # If mid is odd and equals the previous, we are in the correct pattern
                # so we move to the right
                if nums[mid] == nums[mid - 1]:
                    low = mid + 1
                else:
                    high = mid - 1

        # When low == high, we've found the single non-duplicate element
        return nums[low]
