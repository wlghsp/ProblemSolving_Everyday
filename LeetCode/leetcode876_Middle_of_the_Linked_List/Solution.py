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
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def getLength(self, head):
        result = 0
        while head:
            result += 1
            head = head.next
        return result

if __name__ == "__main__":
    sol = Solution()
    print_list(sol.middleNode(make_list([1, 2, 3, 4, 5])))    # [3, 4, 5]
    print_list(sol.middleNode(make_list([1, 2, 3, 4, 5, 6]))) # [4, 5, 6]
