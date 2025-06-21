class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def backtrack(start, path):
            # path is the current subset I have built so far.
            # Append a copy of path to the results list.
            result.append(path[:])  
            
            # Now, adding each of the remaining elements one by one.
            for i in range(start, len(nums)):
                path.append(nums[i])       # Choose this element
                backtrack(i + 1, path)     # Recurse with next elements
                path.pop()                 # Backtrack: remove the element  
        
        backtrack(0, [])
        return result
