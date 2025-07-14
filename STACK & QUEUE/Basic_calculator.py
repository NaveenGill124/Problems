class Solution:
    def calculate(self, s: str) -> int:
        
    
        def into_splits(s):

            splits = []
            num = ""

            for i in s:

                if i.isdigit():
                    num += i
                else:
                    if num:
                        
                        splits.append(num)
                        num = ""
                    if i in ['+', '-', '(', ')']:

                        splits.append(i)
            
            if num:
                splits.append(num)
            
            return splits
            

        def calculate(splits):

            stack = []
            res = 0
            sign = 1


            for i in splits:

                if i.isdigit():

                    res = res + sign * int(i)

                
                elif i == '+':
                    sign = +1

                elif i == '-':
                    sign = -1
                
                elif i == '(':

                    stack.append(res)
                    stack.append(sign)
                    res = 0
                    sign = 1
                
                elif i == ')':

                    prev_sign = stack.pop()
                    prev_res = stack.pop()

                    res = prev_res + prev_sign * res
            
            return res

        
        return calculate(into_splits(s))