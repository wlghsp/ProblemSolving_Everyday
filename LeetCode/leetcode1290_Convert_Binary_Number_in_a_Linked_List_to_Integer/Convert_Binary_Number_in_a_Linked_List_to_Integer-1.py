# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = 0
        while head:
            result = result * 2 + head.val # 왼쪽으로 비트만큼 이동 후 현재 자리 더하기
            head = head.next
        return result

        # bits = []
        # while head:
        #     bits.append(str(head.val))
        #     head = head.next
        # binary_str = ''.join(bits)
        # return int(binary_str, 2)



if __name__ == "__main__":
    nodes = [ListNode(1), ListNode(0), ListNode(1)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    head = nodes[0]

    sol = Solution()
    print(sol.getDecimalValue(head))