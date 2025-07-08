import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        max_day = max(end for _, end in events)
        events.sort()
        event_idx, cnt = 0, 0
        pq = []
        for day in range(1, max_day + 1):
            while event_idx < n and events[event_idx][0] == day:
                heapq.heappush(pq, events[event_idx][1])
                event_idx += 1

            while pq and pq[0] < day:
                heapq.heappop(pq)

            if pq:
                heapq.heappop(pq)
                cnt += 1

        return cnt


if __name__ == "__main__":
    s = Solution()
    print(s.maxEvents([[1,2],[2,3],[3,4]])) # 3
    print(s.maxEvents([[1,2],[2,3],[3,4],[1,2]])) # 4
