# 연결 리스트 노드 정의
from unittest import TestCase

from LeetCode.leetcode2_add_two_numbers.main import Solution


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 헬퍼 함수: 리스트 → 연결 리스트
def list_to_linkedlist(numbers):
    dummy = ListNode()
    current = dummy
    for num in numbers:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# 헬퍼 함수: 연결 리스트 → 리스트
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class TestAddTwoNumbers(TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        l1 = list_to_linkedlist([2, 4, 3])
        l2 = list_to_linkedlist([5, 6, 4])
        expected = [7, 0, 8]
        result = linkedlist_to_list(self.solution.addTwoNumbers(l1, l2))
        self.assertEqual(result, expected)

    def test_example2(self):
        l1 = list_to_linkedlist([0])
        l2 = list_to_linkedlist([0])
        expected = [0]
        result = linkedlist_to_list(self.solution.addTwoNumbers(l1, l2))
        self.assertEqual(result, expected)

    def test_carry_over(self):
        l1 = list_to_linkedlist([9, 9, 9])
        l2 = list_to_linkedlist([1])
        expected = [0, 0, 0, 1]
        result = linkedlist_to_list(self.solution.addTwoNumbers(l1, l2))
        self.assertEqual(result, expected)

    def test_unequal_length(self):
        l1 = list_to_linkedlist([2, 4])
        l2 = list_to_linkedlist([5, 6, 4])
        expected = [7, 0, 5]
        result = linkedlist_to_list(self.solution.addTwoNumbers(l1, l2))
        self.assertEqual(result, expected)