from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            current.next = ListNode(total % 10)
            current = current.next
            carry = total // 10
            
        return dummy.next

# Helper function to create linked list from list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert linked list to list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result1 = solution.addTwoNumbers(l1, l2)
    print(f"Test 1: {linked_list_to_list(result1)}")  # Expected: [7, 0, 8]

    # Test case 2
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result2 = solution.addTwoNumbers(l1, l2)
    print(f"Test 2: {linked_list_to_list(result2)}")  # Expected: [0]

    # Test case 3
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result3 = solution.addTwoNumbers(l1, l2)
    print(f"Test 3: {linked_list_to_list(result3)}")  # Expected: [8, 9, 9, 9, 0, 0, 0, 1]
