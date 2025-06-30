class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        # Since the peak can't be at index 0 or the last index, we set our search bounds inside the array
        high = len(arr) - 2
        low = 1
        
        while low <= high:
            mid = (low + high) // 2  # Get the middle index

            # Check if the current element is greater than both neighbors — that's the peak
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid

            # If the middle is increasing, we're on the left side of the peak → move right
            if arr[mid] > arr[mid - 1]:
                low = mid + 1
            else:
                # If it's decreasing, we're on the right side of the peak → move left
                high = mid - 1
