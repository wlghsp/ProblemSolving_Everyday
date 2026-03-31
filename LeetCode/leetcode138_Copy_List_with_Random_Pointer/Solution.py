"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        curr = head
        node_dict = {}
        while curr:
            node_dict[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                node_dict[curr].next = node_dict[curr.next]
            if curr.random:
                node_dict[curr].random = node_dict[curr.random]
            curr = curr.next
        return node_dict[head]

if __name__ == "__main__":
    # Helper function to create a list from values
    def create_list(values, random_indices):
        """values: 노드 값 리스트, random_indices: 각 노드의 random 포인터 인덱스"""
        if not values:
            return None

        nodes = [Node(val) for val in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        for i, rand_idx in enumerate(random_indices):
            nodes[i].random = nodes[rand_idx] if rand_idx is not None else None

        return nodes[0]

    def list_to_string(head):
        """연결 리스트를 문자열로 변환 (디버깅용)"""
        result = []
        node = head
        visited = set()
        while node and id(node) not in visited:
            visited.add(id(node))
            rand_val = node.random.val if node.random else None
            result.append(f"[{node.val}->{rand_val}]")
            node = node.next
        return " -> ".join(result)

    sol = Solution()

    # Test case 1: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    # 7의 random은 null
    # 13의 random은 7 (index 0)
    # 11의 random은 1 (index 4)
    # 10의 random은 11 (index 2)
    # 1의 random은 7 (index 0)
    head1 = create_list([7, 13, 11, 10, 1], [None, 0, 4, 2, 0])
    copy1 = sol.copyRandomList(head1)
    print(f"Test 1: {list_to_string(copy1)}")
    # Expected: 원본과 같은 구조, 하지만 다른 노드 객체

    # Test case 2: [[1,1],[2,1]]
    # 1의 random은 1 (자기 자신, index 0)
    # 2의 random은 1 (index 0)
    head2 = create_list([1, 2], [0, 0])
    copy2 = sol.copyRandomList(head2)
    print(f"Test 2: {list_to_string(copy2)}")

    # Test case 3: [[3,null]]
    # 3의 random은 null
    head3 = create_list([3], [None])
    copy3 = sol.copyRandomList(head3)
    print(f"Test 3: {list_to_string(copy3)}")

    # Test case 4: None
    head4 = None
    copy4 = sol.copyRandomList(head4)
    print(f"Test 4: {copy4}")  # Expected: None
