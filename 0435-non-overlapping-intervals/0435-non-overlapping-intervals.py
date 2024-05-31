class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 0:
            return 0

        intervals = sorted(intervals, key=lambda x:x[1])
        ans = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if prev_end > intervals[i][0]:
                ans += 1
                prev_end = min(prev_end, intervals[i][1])
            else:
                prev_end = intervals[i][1]
        return ans