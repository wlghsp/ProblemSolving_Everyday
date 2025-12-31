# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 힙 초기화
        heap = []

        # 각 리스트의 첫 노드를 힙에 추가
        for i, node in enumerate(lists):
            if node:
                # (값, 인덱스, 노드) 형태로 저장
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode()
        current = dummy

        while heap:
            # 가장 작은 노드 꺼내기
            val, i, node = heapq.heappop(heap)

            # 결과에 추가
            current.next = node
            # current 이동
            current = current.next
            
            # 다음 노드가 있다면 힙에 추가
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next

    def mergeKLists_divde_and_conquer(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1, l2):
            dummy = ListNode()
            current = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            current.next = l1 if l1 else l2

            return dummy.next
        
        if not lists:
            return None
        
        # 리스트가 1개 남을 때까지 반복
        while len(lists) > 1:
            merged = []

            # 두 개씩 짝지어서 합치기
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(mergeTwoLists(l1, l2))
            
            lists = merged

        return lists[0]
                
    
    def mergeKLists_brute(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []

        for linked_list in lists:
            current = linked_list
            while current:
                values.append(current.val)
                current = current.next
        values.sort()
        dummy = ListNode()
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next





if __name__ == "__main__":
    def create_linked_list(values: List[int]) -> Optional[ListNode]:
        """리스트로부터 연결 리스트 생성"""
        if not values:
            return None

        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head


    def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
        """연결 리스트를 리스트로 변환"""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    solution = Solution()

    # Test case 1: 기본 예제
    lists1 = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    result1 = solution.mergeKLists(lists1)
    print(f"Test 1: {linked_list_to_list(result1)}")
    print(f"Expected: [1, 1, 2, 3, 4, 4, 5, 6]")
    print()

    # Test case 2: 빈 리스트
    lists2 = []
    result2 = solution.mergeKLists(lists2)
    print(f"Test 2: {linked_list_to_list(result2)}")
    print(f"Expected: []")
    print()

    # Test case 3: 빈 연결 리스트가 포함된 경우
    lists3 = [create_linked_list([])]
    result3 = solution.mergeKLists(lists3)
    print(f"Test 3: {linked_list_to_list(result3)}")
    print(f"Expected: []")
    print()

    # Test case 4: 하나의 연결 리스트만 있는 경우
    lists4 = [create_linked_list([1, 2, 3])]
    result4 = solution.mergeKLists(lists4)
    print(f"Test 4: {linked_list_to_list(result4)}")
    print(f"Expected: [1, 2, 3]")
    print()

    # Test case 5: 여러 개의 연결 리스트
    lists5 = [
        create_linked_list([1]),
        create_linked_list([0]),
        create_linked_list([2])
    ]
    result5 = solution.mergeKLists(lists5)
    print(f"Test 5: {linked_list_to_list(result5)}")
    print(f"Expected: [0, 1, 2]")
    print()

    # Test case 6: 음수 값 포함
    lists6 = [
        create_linked_list([-2, -1, -1]),
        create_linked_list([-3, 1])
    ]
    result6 = solution.mergeKLists(lists6)
    print(f"Test 6: {linked_list_to_list(result6)}")
    print(f"Expected: [-3, -2, -1, -1, 1]")
    print()


