from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    def build(vals):
        dummy = ListNode(0)
        cur = dummy
        for v in vals:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    def to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    s = Solution()
    print(to_list(s.removeNthFromEnd(build([1, 2, 3, 4, 5]), 2)))  # [1, 2, 3, 5]
    print(to_list(s.removeNthFromEnd(build([1]), 1)))              # []
    print(to_list(s.removeNthFromEnd(build([1, 2]), 1)))           # [1]
