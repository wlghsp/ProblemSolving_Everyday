class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.nums = self.getNums(root)
        self.current = 0

    def next(self) -> int:
        result = self.nums[self.current]
        self.current += 1
        return result

    def hasNext(self) -> bool:
        return len(self.nums) > self.current
    

    def getNums(self, root: TreeNode):
        result = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)
        return result

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
