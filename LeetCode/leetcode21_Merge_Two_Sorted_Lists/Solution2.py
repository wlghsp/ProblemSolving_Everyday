from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next

# Helper functions
def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result1 = solution.mergeTwoLists(build_list([1, 2, 4]), build_list([1, 3, 4]))
    print(f"Test 1: {to_array(result1)}")  # Expected: [1, 1, 2, 3, 4, 4]

    # Test case 2
    result2 = solution.mergeTwoLists(build_list([]), build_list([]))
    print(f"Test 2: {to_array(result2)}")  # Expected: []

    # Test case 3
    result3 = solution.mergeTwoLists(build_list([]), build_list([0]))
    print(f"Test 3: {to_array(result3)}")  # Expected: [0]

    # Test case 4
    result4 = solution.mergeTwoLists(build_list([5]), build_list([1, 2, 4]))
    print(f"Test 4: {to_array(result4)}")  # Expected: [1, 2, 4, 5]
