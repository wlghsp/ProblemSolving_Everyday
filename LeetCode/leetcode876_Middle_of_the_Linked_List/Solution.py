# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        # 토끼와 거북이 (two pointers)
        핵심개념
        - 거북이 slow = 한 칸씩 이동
        - 토끼 fast = 두 칸씩 이동
        - 토끼가 끝에 도달하면 거북이는 정확히 중간에 위치! 
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    def middleNode_two_traverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        핵심 개념
        - 길이를 구한다.
        - 중간까지 이동시키고 이를 리턴한다
        """
        count = 0
        current = head
        # 1단계: 길이 세기
        while current:
            count += 1
            current = current.next
        
        # 2단계: 중간까지 이동
        middle_pos = count // 2
        current = head
        for i in range(middle_pos):
            current = current.next
        return current



