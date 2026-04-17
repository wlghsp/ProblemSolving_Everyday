from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        keep, prev = 0, float('-inf')
        for start, end in intervals:
            if start >= prev:
                keep += 1
                prev = end

        return len(intervals) - keep



if __name__ == "__main__":
    s = Solution()

    # Example 1: Expected 1
    print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))

    # Example 2: Expected 2
    print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))

    # Example 3: Expected 0
    print(s.eraseOverlapIntervals([[1,2],[2,3]]))
