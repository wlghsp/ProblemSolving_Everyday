from typing import Optional

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

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                # 같다면 다음 노드에 그 다음 노드를 할당하여 다음 노드 중복 제거
                curr.next = curr.next.next
            else:
                # 다르므로 1칸 이동
                curr = curr.next

        return head

if __name__ == "__main__":
    sol = Solution()

    # Test 1: [1,1,2] → [1,2]
    print(print_list(sol.deleteDuplicates(make_list([1,1,2]))))  # [1, 2]

    # Test 2: [1,1,2,3,3] → [1,2,3]
    print(print_list(sol.deleteDuplicates(make_list([1,1,2,3,3]))))  # [1, 2, 3]

    # Test 3: [] → []
    print(print_list(sol.deleteDuplicates(None)))  # []
