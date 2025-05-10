class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []

        intervals.sort()

        result = []

        curr_start, curr_end = intervals[0]

        for start, end in intervals[1:]:

            if start <= curr_end:
                curr_end = max(end, curr_end)
            else:

                result.append([curr_start, curr_end])
                curr_start, curr_end = start, end

        
        result.append([curr_start, curr_end])
        return result


        
