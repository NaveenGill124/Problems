class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        comb = []
        candidates.sort()

        def combSum(arr, idx, target):
            if target == 0:
                result.append(comb[:])
                return
            if idx == len(arr) or target < 0:
                return

            # Pick the current element
            comb.append(arr[idx])
            combSum(arr, idx, target - arr[idx])
            comb.pop()

            # Skip the current element
            combSum(arr, idx + 1, target)

        combSum(candidates, 0, target)
        return result
