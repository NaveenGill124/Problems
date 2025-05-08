class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        final_result = []
        for row in range(numRows):

            if row == 0:
                final_result.append([1])
            else:
                prev = final_result[-1]
                new_row = [1]

                for i in range(len(prev)-1):
                    new_row.append(prev[i] + prev[i+1])

                new_row.append(1)
            
                final_result.append(new_row)

        return final_result

