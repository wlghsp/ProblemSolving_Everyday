class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()

    # Test 1: [3,2,0,-4], pos=1 (사이클: -4 → 2)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # 사이클!
    print(sol.hasCycle(node1))  # Expected: True

    # Test 2: [1,2], pos=0 (사이클: 2 → 1)
    node5 = ListNode(1)
    node6 = ListNode(2)
    node5.next = node6
    node6.next = node5  # 사이클!
    print(sol.hasCycle(node5))  # Expected: True

    # Test 3: [1], pos=-1 (사이클 없음)
    node7 = ListNode(1)
    print(sol.hasCycle(node7))  # Expected: False
