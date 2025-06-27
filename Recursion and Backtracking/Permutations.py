class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        n = len(nums)
        def revert(nums, idx, result):

            if idx == n:

                result.append(nums[:])
                return

            for i in range(idx, n):

                nums[idx], nums[i] = nums[i], nums[idx]

                revert(nums, idx+1, result)

                nums[idx], nums[i] = nums[i], nums[idx]

        revert(nums, 0, result)

        return result
