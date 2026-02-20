from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        
        return dummy.next


if __name__ == "__main__":
    sol = Solution()

    print_list(sol.removeNthFromEnd(make_list([1,2,3,4,5]), 2))  # Expected: [1,2,3,5]
    print_list(sol.removeNthFromEnd(make_list([1]), 1))           # Expected: []
    print_list(sol.removeNthFromEnd(make_list([1,2]), 1))         # Expected: [1]
