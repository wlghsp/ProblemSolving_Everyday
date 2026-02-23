from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 1. 둘의 길이를 구한다
        a_len = self.getLength(headA)
        b_len = self.getLength(headB)
        
        # 2. 길이가 긴쪽을 그 차이만큼 전진
        if a_len > b_len:
            for _ in range(a_len - b_len):
                headA = headA.next
            
        elif a_len < b_len:
             for _ in range(b_len - a_len):
                headB = headB.next
        
        # 3. 둘이 동시에 전진하여 같은 노드를 만나면 break
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA
        
        
    def getLength(self, head):
        result = 0
        while head:
            result += 1
            head = head.next
        return result


def build_intersecting_lists(listA, listB, skipA, skipB):
    """두 리스트가 특정 노드에서 교차하는 구조 생성"""
    nodesA = [ListNode(v) for v in listA]
    nodesB = [ListNode(v) for v in listB[:skipB]]

    for i in range(len(nodesA) - 1):
        nodesA[i].next = nodesA[i + 1]
    for i in range(len(nodesB) - 1):
        nodesB[i].next = nodesB[i + 1]

    # 교차 연결
    if skipA < len(nodesA) and nodesB:
        nodesB[-1].next = nodesA[skipA]

    headA = nodesA[0] if nodesA else None
    headB = nodesB[0] if nodesB else None
    intersect = nodesA[skipA] if skipA < len(nodesA) else None
    return headA, headB, intersect


if __name__ == "__main__":
    # Example 1: intersectVal=8, listA=[4,1,8,4,5], listB=[5,6,1,8,4,5], skipA=2, skipB=3
    # 교차 노드: val=8
    headA, headB, expected = build_intersecting_lists([4,1,8,4,5], [5,6,1,8,4,5], skipA=2, skipB=3)
    result = Solution().getIntersectionNode(headA, headB)
    print(result.val if result else None)  # Expected: 8

    # Example 2: intersectVal=2, listA=[1,9,1,2,4], listB=[3,2,4], skipA=3, skipB=1
    headA, headB, expected = build_intersecting_lists([1,9,1,2,4], [3,2,4], skipA=3, skipB=1)
    result = Solution().getIntersectionNode(headA, headB)
    print(result.val if result else None)  # Expected: 2

    # Example 3: no intersection
    headA, headB, expected = build_intersecting_lists([2,6,4], [1,5], skipA=3, skipB=2)
    result = Solution().getIntersectionNode(headA, headB)
    print(result.val if result else None)  # Expected: None
