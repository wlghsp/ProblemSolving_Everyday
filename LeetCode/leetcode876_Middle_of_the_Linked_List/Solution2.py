from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    sol = Solution()

    def make_list(vals):
        dummy = ListNode(0)
        cur = dummy
        for v in vals:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    def print_list(node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        print(res)

    # Test 1: [1,2,3,4,5] → [3,4,5]
    print_list(sol.middleNode(make_list([1,2,3,4,5])))

    # Test 2: [1,2,3,4,5,6] → [4,5,6]
    print_list(sol.middleNode(make_list([1,2,3,4,5,6])))

    # Test 3: [1] → [1]
    print_list(sol.middleNode(make_list([1])))
