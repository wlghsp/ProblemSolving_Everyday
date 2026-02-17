class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node
        return prev        


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    sol = Solution()

    # Test 1: head = [1,2,3,4,5]
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = sol.reverseList(head1)
    print(linked_list_to_list(result1))  # Expected: [5,4,3,2,1]

    # Test 2: head = [1,2]
    head2 = create_linked_list([1, 2])
    result2 = sol.reverseList(head2)
    print(linked_list_to_list(result2))  # Expected: [2,1]

    # Test 3: head = []
    head3 = create_linked_list([])
    result3 = sol.reverseList(head3)
    print(linked_list_to_list(result3))  # Expected: []
