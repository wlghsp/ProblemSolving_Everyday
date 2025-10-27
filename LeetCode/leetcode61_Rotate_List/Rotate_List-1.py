# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # 1. 리스트 길이 구하기
        length = 0
        current = head
        while current.next:
            current = current.next
            length += 1

        # 2. k가 length 이상이면 나머지만큼 회전
        k = k % length
        if k == 0:
            return head

        # 3. 마지막 노드를 head에 연결해서 원형 리스트로
        current.next = head

        # 4. (length - k) 번째 노드 찾기 (새 head 바로 앞
        steps = length - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # 4. 원형 단절
        new_tail.next = None

        return new_head

if __name__ == "__main__":
    sol = Solution()
