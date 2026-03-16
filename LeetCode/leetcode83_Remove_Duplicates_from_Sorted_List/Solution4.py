from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        # 현재와 다음이 존재하는지 확인
        # 현재와 다음의 값이 같으면 2칸 이동, 아니면 1칸 이동
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head


# Helper functions
def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    s = Solution()

    # Example 1: [1,1,2] → [1,2]
    head = build_list([1, 1, 2])
    print(list_to_array(s.deleteDuplicates(head)))  # [1, 2]

    # Example 2: [1,1,2,3,3] → [1,2,3]
    head = build_list([1, 1, 2, 3, 3])
    print(list_to_array(s.deleteDuplicates(head)))  # [1, 2, 3]

    # Edge: single element
    head = build_list([1])
    print(list_to_array(s.deleteDuplicates(head)))  # [1]

    # Edge: all duplicates
    head = build_list([1, 1, 1])
    print(list_to_array(s.deleteDuplicates(head)))  # [1]
