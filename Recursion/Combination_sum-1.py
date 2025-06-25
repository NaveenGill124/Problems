class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        results = []   
        comb = []       

        def backtrack(idx: int, target_left: int) -> None:
            
            # Base case: if we hit the target sum exactly
            if target_left == 0:
                results.append(comb[:])  # Append a copy of current combination
                return

            # Base case: if we exhaust candidates or overshoot target
            if target_left < 0 or idx == len(candidates):
                return

            # ---- include the current number ----
            comb.append(candidates[idx])
            # Stay on the same index because we can reuse the number
            backtrack(idx, target_left - candidates[idx])

            # Backtrack — remove the last number added
            comb.pop()

            # ---- skip the current number ----
            backtrack(idx + 1, target_left)

        # Kick off the recursion
        backtrack(0, target)

        # Use a set to remove duplicate combinations if any (e.g. different orderings)
        # Tuples are hashable so we can add them to a set
        unique_combinations = {tuple(sorted(subset)) for subset in results}

        # Convert each tuple back to a list
        final_result = [list(comb) for comb in unique_combinations]

        return final_result
