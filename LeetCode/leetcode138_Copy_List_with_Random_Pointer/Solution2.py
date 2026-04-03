"""
138. Copy List with Random Pointer (Medium)
https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n
brand new nodes, where each new node has its value set to the value of its
corresponding original node. Both the next and random pointer of the new nodes
should point to new nodes in the copied list such that the pointers in the
original list and copied list represent the same list state. None of the
pointers in the new list should point to nodes in the original list.
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        node_dict = {}
        curr = head
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
    def create_list(values, random_indices):
        if not values:
            return None
        nodes = [Node(val) for val in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        for i, rand_idx in enumerate(random_indices):
            nodes[i].random = nodes[rand_idx] if rand_idx is not None else None
        return nodes[0]

    def list_to_string(head):
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

    # Test 1: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    head1 = create_list([7, 13, 11, 10, 1], [None, 0, 4, 2, 0])
    copy1 = sol.copyRandomList(head1)
    print(f"Test 1: {list_to_string(copy1)}")
    # Expected: [7->None] -> [13->7] -> [11->1] -> [10->11] -> [1->7]

    # Test 2: [[1,1],[2,1]]
    head2 = create_list([1, 2], [0, 0])
    copy2 = sol.copyRandomList(head2)
    print(f"Test 2: {list_to_string(copy2)}")
    # Expected: [1->1] -> [2->1]

    # Test 3: [[3,null]]
    head3 = create_list([3], [None])
    copy3 = sol.copyRandomList(head3)
    print(f"Test 3: {list_to_string(copy3)}")
    # Expected: [3->None]

    # Test 4: None
    copy4 = sol.copyRandomList(None)
    print(f"Test 4: {copy4}")
    # Expected: None
