class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
       
        n = len(nums)

       # we are going to solve this in 3 steps
        # 1) Find the pivot: the first index from the end
        #    where nums[i] < nums[i+1].
        piv = -1
        for i in range(n - 2, -1, -1):      # i = n-2, n-3, ..., 0
            if nums[i] < nums[i + 1]:
                piv = i
                break
        
        # If no pivot, the sequence is descending → reverse all to get smallest
        if piv == -1:
            nums.reverse()
            return
        
        # 2) Find the smallest element > nums[piv] to the right of piv
        #    (scan from the end to find the first one > pivot)
        for j in range(n - 1, piv, -1):
            if nums[j] > nums[piv]:
                # 3) Swap with pivot
                nums[piv], nums[j] = nums[j], nums[piv]
                break
        
        # 4) Reverse the tail (everything right of the pivot) to get the next permutation
        #    (since that tail was in descending order, reversing it makes it ascending)
        left, right = piv + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
