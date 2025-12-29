# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # (2) 재귀 풀이
        # 베이스 케이스: 빈 리스트 or 노드 1개
        if not head or not head.next:
            return head
        
        # 나머지를 뒤집기 (재귀)
        new_head = self.reverseList(head.next)

        # 현재 노드를 끝에 연결
        head.next.next = head
        head.next = None

        return new_head

    def reverseList_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # (1) 반복문 풀이
        prev = None # 이전 노드 (처음엔 None)
        current = head # 현재 노드 (처음엔 head)

        while current: # current 가 None 이면 종료 = 끝에 도달
            # 1. 다음 노드 임시 저장 (끊어지기 전에!)
            next_temp = current.next

            # 2. 화살표 뒤집기
            current.next = prev

            # 3. 한 칸씩 전진
            prev = current
            current = next_temp

        return prev # prev가 새로운 head !



