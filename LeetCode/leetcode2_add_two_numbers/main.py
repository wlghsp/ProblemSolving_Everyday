# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

def list_to_linkedlist(numbers):
    dummy = ListNode()
    current = dummy
    for num in numbers:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 결과를 저장할 연결 리스트의 더미 노드(가짜 노드)를 만든다.
        # 실제 결과는 dummy.next 부터 시작된다.
        dummy = ListNode()
        current = dummy # 현재 위치를 가리키는 포인터, 처음에는 dummy를 가리킴
        carry = 0 # 올림 수를 저장하는 변수 (예: 9 + 8 = 17 이면 carry 는 1)

        while l1 or l2 or carry:
            # l1과 l2가 존재한다면 그 값을 가져오고, 없다면 0으로 간주
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # 두 값과 올림 수를 더해서 총합을 계산
            total = val1 + val2 + carry
            carry = total // 10  # 10으로 나눈 몫이 다음 자리로 올라갈 올림 수
            current.next = ListNode(total % 10) # 현재 자릿수의 값만 노드로 만들어 연결
            current = current.next # current를 다음 노드로 이동

            # l1과 l2가 남아있다면 다음 노드로 이동
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # 결과 연결 리스트의 시작은 dummy.next 부터
        return dummy.next