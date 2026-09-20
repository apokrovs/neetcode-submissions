class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x:x[0])
        intervals2 = []

        curr_start = intervals[0][0]
        curr_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start > curr_end:
                # new interval
                intervals2.append([curr_start, curr_end])
                curr_start = start
                curr_end = end
            else:
                curr_end = max(curr_end, end)
        intervals2.append([curr_start, curr_end])
        return intervals2




        