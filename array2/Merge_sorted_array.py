class Solution:
    def merge(self, nums1: List[int], m: int,
                    nums2: List[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2)



#--------------------Naive approach----------------

class Solution:
    def merge(self, nums1: List[int], m: int,
                    nums2: List[int], n: int) -> None:
        
        x = m - 1
        y = n - 1
        k = m+n -1

        while y>=0:

            if x>=0 and nums1[x]>= nums2[y]:
                nums1[k] = nums1[x]
                x = x-1

            else:
                nums1[k] = nums2[y]
                y = y-1
            
            k = k-1


#---------------this is optimal solution with time complexity: O(m + n)	and space complexity: O(1)----------------------------------
