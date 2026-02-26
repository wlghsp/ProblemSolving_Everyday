class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.vals = []
        self.inorder(root)
        self.curr = 0
        self.length = len(self.vals)

    def next(self) -> int:
        result = 0
        if self.curr < self.length:
            result = self.vals[self.curr]
            self.curr += 1
        return result

    def hasNext(self) -> bool:
        return self.curr < self.length
    
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.vals.append(node.val)
        self.inorder(node.right)



if __name__ == "__main__":
    # Test: root=[7,3,15,null,null,9,20]
    #        7
    #       / \
    #      3  15
    #        /  \
    #       9   20
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    it = BSTIterator(root)
    print(it.next())     # 3
    print(it.next())     # 7
    print(it.hasNext())  # True
    print(it.next())     # 9
    print(it.hasNext())  # True
    print(it.next())     # 15
    print(it.hasNext())  # True
    print(it.next())     # 20
    print(it.hasNext())  # False
