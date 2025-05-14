#-------------------------simple but not affective solution-------------
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        curr_len, max_len = 1, 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue  # skip duplicates
            elif nums[i] == nums[i - 1] + 1:
                curr_len += 1
            else:
                max_len = max(curr_len, max_len)
                curr_len = 1
        
        return max(max_len, curr_len)

# -------------------optimal solution with O(n) time complexity---------------

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0

        num_set = set(nums)

        for num in num_set:

            if num-1 not in num_set:

                acc_num = num

                pre_num = 1

                while acc_num + 1 in num_set:

                    acc_num += 1
                    pre_num += 1
        
                result = max(result, pre_num)

        return result
