class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_list(lst):
    dummy = ListNode()
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head

        while curr:
            if curr and curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

if __name__ == "__main__":
    sol = Solution()
    print_list(sol.deleteDuplicates(make_list([1, 1, 2])))        # [1, 2]
    print_list(sol.deleteDuplicates(make_list([1, 1, 2, 3, 3]))) # [1, 2, 3]
