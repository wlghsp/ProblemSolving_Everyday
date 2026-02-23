from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymme(root.left, root.right)
    
    def isSymme(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSymme(p.left, q.right) and self.isSymme(p.right, q.left)        
    

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
    # Example 1: [1,2,2,3,4,4,3] -> True
    root1 = build_tree([1, 2, 2, 3, 4, 4, 3])
    print(Solution().isSymmetric(root1))  # Expected: True

    # Example 2: [1,2,2,null,3,null,3] -> False
    root2 = build_tree([1, 2, 2, None, 3, None, 3])
    print(Solution().isSymmetric(root2))  # Expected: False
