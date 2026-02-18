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


def list_to_arr(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
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

    # Test 1: [1,2,3,4,5], n=2 → [1,2,3,5]
    print(list_to_arr(sol.removeNthFromEnd(make_list([1,2,3,4,5]), 2)))  # [1,2,3,5]

    # Test 2: [1], n=1 → []
    print(list_to_arr(sol.removeNthFromEnd(make_list([1]), 1)))  # []

    # Test 3: [1,2], n=1 → [1]
    print(list_to_arr(sol.removeNthFromEnd(make_list([1,2]), 1)))  # [1]
