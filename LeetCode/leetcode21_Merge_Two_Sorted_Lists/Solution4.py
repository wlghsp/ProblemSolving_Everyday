class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    # Test 1: list1 = [1,2,4], list2 = [1,3,4]
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    print(linked_list_to_list(sol.mergeTwoLists(list1, list2)))  # [1,1,2,3,4,4]

    # Test 2: list1 = [], list2 = []
    print(linked_list_to_list(sol.mergeTwoLists(None, None)))  # []

    # Test 3: list1 = [], list2 = [0]
    list3 = create_linked_list([0])
    print(linked_list_to_list(sol.mergeTwoLists(None, list3)))  # [0]
