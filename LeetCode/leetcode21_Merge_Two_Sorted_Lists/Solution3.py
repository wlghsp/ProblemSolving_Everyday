class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def make_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2

        return dummy.next
            



if __name__ == "__main__":
    sol = Solution()

    # Test 1: [1,2,4] + [1,3,4] → [1,1,2,3,4,4]
    l1 = make_list([1, 2, 4])
    l2 = make_list([1, 3, 4])
    print(to_list(sol.mergeTwoLists(l1, l2)))  # [1,1,2,3,4,4]

    # Test 2: [] + [] → []
    print(to_list(sol.mergeTwoLists(None, None)))  # []

    # Test 3: [] + [0] → [0]
    l3 = make_list([0])
    print(to_list(sol.mergeTwoLists(None, l3)))  # [0]
