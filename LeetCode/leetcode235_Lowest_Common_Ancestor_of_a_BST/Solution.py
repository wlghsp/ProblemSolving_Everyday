class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root



def build_tree(values):
    """Build tree from level-order list (None represents missing nodes)"""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def find_node(root, val):
    """Find node with given value in BST"""
    if not root:
        return None
    if root.val == val:
        return root
    if root.val < val:
        return find_node(root.right, val)
    return find_node(root.left, val)


if __name__ == "__main__":
    sol = Solution()

    # Test 1: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    root1 = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p1 = find_node(root1, 2)
    q1 = find_node(root1, 8)
    result1 = sol.lowestCommonAncestor(root1, p1, q1)
    print(result1.val)  # Expected: 6

    # Test 2: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    root2 = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p2 = find_node(root2, 2)
    q2 = find_node(root2, 4)
    result2 = sol.lowestCommonAncestor(root2, p2, q2)
    print(result2.val)  # Expected: 2 (p 자신이 조상)

    # Test 3: root = [2,1], p = 2, q = 1
    root3 = build_tree([2, 1])
    p3 = find_node(root3, 2)
    q3 = find_node(root3, 1)
    result3 = sol.lowestCommonAncestor(root3, p3, q3)
    print(result3.val)  # Expected: 2
