class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        
        result = 0
        
        if root.val < low:
            result += self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            result += self.rangeSumBST(root.left, low, high)
        else:
            result += root.val
            result += self.rangeSumBST(root.right, low, high)
            result += self.rangeSumBST(root.left, low, high)

        return result



if __name__ == "__main__":
    sol = Solution()

    # Test 1: root=[10,5,15,3,7,null,18], low=7, high=15 → 32
    #        10
    #       /  \
    #      5   15
    #     / \    \
    #    3   7   18
    root1 = TreeNode(10)
    root1.left = TreeNode(5)
    root1.right = TreeNode(15)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(7)
    root1.right.right = TreeNode(18)
    print(sol.rangeSumBST(root1, 7, 15))  # 32

    # Test 2: root=[10,5,15,3,7,13,18,1,null,6], low=6, high=10 → 23
    root2 = TreeNode(10)
    root2.left = TreeNode(5)
    root2.right = TreeNode(15)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(7)
    root2.right.left = TreeNode(13)
    root2.right.right = TreeNode(18)
    root2.left.left.left = TreeNode(1)
    root2.left.right.left = TreeNode(6)
    print(sol.rangeSumBST(root2, 6, 10))  # 23
