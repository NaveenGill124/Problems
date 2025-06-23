from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort() # Sort so duplicate subsets will have the same order
        result = []
        
        def backtrack(index: int, path: List[int]) -> None:
            # Once we hit the end of the list, we're adding the current path
            if index == len(nums):
                result.append(path.copy())
                return
            # we have two options
            # Option 1: Don't include nums[index]
            backtrack(index + 1, path)
            
            # Option 2: Include nums[index]
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()  # backtrack/remove the last number
        
        # Generate all subsets
        backtrack(0, [])
        
        # Remove duplicate subsets using set of tuples
        unique_subsets = set()
        for subset in result:
            unique_subsets.add(tuple(subset))
        
        # Convert each tuple back to list
        final_result = []
        for subset in unique_subsets:
            final_result.append(list(subset))
        
        return final_result

