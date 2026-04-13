class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # 1단계: 끼워넣기
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next.next  # 원본 다음으로
            
        # 2단계: random 연결
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # 3단계: 분리
        curr = head
        new_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            copy.next = copy.next.next if copy.next else None
            curr = curr.next
        
        return new_head

if __name__ == "__main__":
    sol = Solution()

    # 케이스 1: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    n1 = Node(7)
    n2 = Node(13)
    n3 = Node(11)
    n4 = Node(10)
    n5 = Node(1)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n5
    n1.random = None
    n2.random = n1
    n3.random = n5
    n4.random = n3
    n5.random = n1

    result = sol.copyRandomList(n1)
    cur = result
    while cur:
        print(f"val={cur.val}, random={cur.random.val if cur.random else None}")
        cur = cur.next
    # 기대: 7→None, 13→7, 11→1, 10→11, 1→7

    print()

    # 케이스 2: [[1,1],[2,1]]
    a1 = Node(1)
    a2 = Node(2)
    a1.next = a2
    a1.random = a2
    a2.random = a2

    result2 = sol.copyRandomList(a1)
    cur = result2
    while cur:
        print(f"val={cur.val}, random={cur.random.val if cur.random else None}")
        cur = cur.next
