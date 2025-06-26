class Solution:
    def partition(self, s: str) -> List[List[str]]:


        result = []
        arr = []

        def palindrome(sub):
            return sub == sub[::-1]

        def backtrack(idx: int):

            if idx == len(s):
                result.append(arr[:])
                return

            for i in range(idx + 1, len(s) + 1):
                substring = s[idx:i]
                if palindrome(substring):
                    arr.append(substring)
                    backtrack(i)
                    arr.pop()

        backtrack(0)
        return result
