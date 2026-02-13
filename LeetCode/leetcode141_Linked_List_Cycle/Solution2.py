from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


# Helper functions
def build_cycle_list(arr, pos):
    if not arr:
        return None
    nodes = [ListNode(val) for val in arr]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: [3,2,0,-4], cycle at pos 1
    head1 = build_cycle_list([3, 2, 0, -4], 1)
    print(f"Test 1: {solution.hasCycle(head1)}")  # Expected: True

    # Test case 2: [1,2], cycle at pos 0
    head2 = build_cycle_list([1, 2], 0)
    print(f"Test 2: {solution.hasCycle(head2)}")  # Expected: True

    # Test case 3: [1], no cycle
    head3 = build_cycle_list([1], -1)
    print(f"Test 3: {solution.hasCycle(head3)}")  # Expected: False

    # Test case 4: empty list
    head4 = build_cycle_list([], -1)
    print(f"Test 4: {solution.hasCycle(head4)}")  # Expected: False
