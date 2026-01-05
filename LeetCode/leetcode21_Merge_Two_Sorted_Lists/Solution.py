# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 두 리스트 중 작은 값을 선택하고, 그 다음은 재귀에게 맡긴다.
        if list1 is None:
           return list2
        if list2 is None:
           return list1
       
        if list1.val <= list2.val:
           # 작은 노드 뒤로 나머지를 정렬된 상태로 반환
           list1.next = self.mergeTwoLists(list1.next, list2)
           return list1
        
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2
       
    
    def mergeTwoLists_iterative(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        LeetCode 21. Merge Two Sorted Lists

        두 개의 정렬된 연결 리스트를 하나의 정렬된 연결 리스트로 병합

        시간복잡도: O(n + m) - 두 리스트의 모든 노드를 한 번씩 순회
        공간복잡도: O(1) - 추가 공간 사용 없음 (재귀 풀이는 O(n + m))
        """
        dummy = ListNode()
        current = dummy 

        # 비교하면서 연결
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # current 포인터를 다음 노드로 이동

        current.next = list1 if list1 else list2

        return dummy.next


# 헬퍼 함수: 리스트 생성
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# 헬퍼 함수: 리스트 출력
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values) if values else "[]"


# 테스트 케이스
if __name__ == "__main__":
    solution = Solution()

    # 테스트 1: list1 = [1,2,4], list2 = [1,3,4]
    print("테스트 1:")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    print(f"list1: {print_linked_list(list1)}")
    print(f"list2: {print_linked_list(list2)}")
    result = solution.mergeTwoLists(list1, list2)
    print(f"결과: {print_linked_list(result)}")
    print(f"예상: 1 -> 1 -> 2 -> 3 -> 4 -> 4\n")

    # 테스트 2: list1 = [], list2 = []
    print("테스트 2:")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    print(f"list1: {print_linked_list(list1)}")
    print(f"list2: {print_linked_list(list2)}")
    result = solution.mergeTwoLists(list1, list2)
    print(f"결과: {print_linked_list(result)}")
    print(f"예상: []\n")

    # 테스트 3: list1 = [], list2 = [0]
    print("테스트 3:")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    print(f"list1: {print_linked_list(list1)}")
    print(f"list2: {print_linked_list(list2)}")
    result = solution.mergeTwoLists(list1, list2)
    print(f"결과: {print_linked_list(result)}")
    print(f"예상: 0\n")

    # 테스트 4: list1 = [5], list2 = [1,2,4]
    print("테스트 4:")
    list1 = create_linked_list([5])
    list2 = create_linked_list([1, 2, 4])
    print(f"list1: {print_linked_list(list1)}")
    print(f"list2: {print_linked_list(list2)}")
    result = solution.mergeTwoLists(list1, list2)
    print(f"결과: {print_linked_list(result)}")
    print(f"예상: 1 -> 2 -> 4 -> 5\n")
