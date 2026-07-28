class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0
        while i < len(intervals):
            low = intervals[i][0]
            high = intervals[i][1]
            while i + 1 < len(intervals) and high >= intervals[i + 1][0]:
                high = max(high, intervals[i + 1][1])
                i += 1
            res.append([low, high])
            i += 1
        return res