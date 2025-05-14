#--------------------Brut-force approach---------------------
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        result = 0

        for i in range(n):

            store_set = set()

            for j in range(i,n):
                if s[j] in store_set:
                    break
                
                store_set.add(s[j])

                result = max(result, j-i+1)
        
        return result

  #---------------------Better solutiion using string slicing-------------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        result = 0
        l = 0

        for r in range(n):

            while s[r] in s[l:r]:

                l +=1
            
            store_res = r - l + 1

            result = max(result, store_res)
        
        return result

#--------------------------------optimal solution is this-------------------------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        result = 0
        
        # using dictonary
        dic = {}

        l = 0

        for r in range(len(s)):

            ch = s[r]

            if ch in dic and dic[ch] >= l:

                l = dic[ch] + 1
            
            dic[ch] = r

            curr_result = r - l + 1

            result = max(result, curr_result)

        return result
