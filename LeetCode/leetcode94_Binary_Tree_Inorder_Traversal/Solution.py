class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        result = []
        
        inorder(root)
        return result   
   


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    sol = Solution()

    # Test 1: root = [1,null,2,3]
    root1 = build_tree([1, None, 2, 3])
    print(sol.inorderTraversal(root1))  # Expected: [1,3,2]

    # Test 2: root = []
    root2 = build_tree([])
    print(sol.inorderTraversal(root2))  # Expected: []

    # Test 3: root = [1]
    root3 = build_tree([1])
    print(sol.inorderTraversal(root3))  # Expected: [1]

    # Test 4: root = [4,2,6,1,3]
    root4 = build_tree([4, 2, 6, 1, 3])
    print(sol.inorderTraversal(root4))  # Expected: [1,2,3,4,6]
