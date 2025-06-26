class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        n = len(candidates)

        result = []   
        comb = []       

        def comSum(idx, t, arr):

            if t == 0:
                result.append(arr[:])
                return
            
            if t < 0 or idx == n:
                return
            
            for i in range(idx, n):

                if i> idx and candidates[i] == candidates[i-1]:
                    continue

                arr.append(candidates[i])

                comSum(i+1, t-candidates[i], arr)

                arr.pop()
        
        comSum(0, target, [])

        
        return result
