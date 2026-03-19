from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                # 값이 같다면 next를 next의 next로 교체하여 다시 비교하게 함
                current.next = current.next.next
            else: # 다르므로 1칸 전진
                current = current.next 
        return head

def build(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    s = Solution()
    print(to_list(s.deleteDuplicates(build([1, 1, 2]))))        # [1, 2]
    print(to_list(s.deleteDuplicates(build([1, 1, 2, 3, 3]))))  # [1, 2, 3]
    print(to_list(s.deleteDuplicates(build([]))))               # []
