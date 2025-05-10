#--------------------------------Majority Element------------------------------------n/2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count_dic = {}

        for i in nums:

            if i in count_dic:
                count_dic[i] +=1
            else:
                count_dic[i] = 1
        

        for i, count in count_dic.items():

            if count > (len(nums))/2:
                return i


#---------------------------------Majority Element II--------------------------------n/3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count_dic = {}

        for i in nums:

            if i in count_dic:
                count_dic[i] +=1
            else:
                count_dic[i] = 1
        
        result = []

        for i, count in count_dic.items():

            if count > (len(nums))//3:
                result.append(i)
        
        return result
