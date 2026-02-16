class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        result = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)

        min_diff = float('inf')
        for i in range(1, len(result)):
            min_diff = min(min_diff, result[i] - result[i - 1])
        return min_diff

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

    # Test 1: root = [4,2,6,1,3]
    root1 = build_tree([4, 2, 6, 1, 3])
    print(sol.getMinimumDifference(root1))  # Expected: 1

    # Test 2: root = [1,0,48,null,null,12,49]
    root2 = build_tree([1, 0, 48, None, None, 12, 49])
    print(sol.getMinimumDifference(root2))  # Expected: 1

    # Test 3: root = [236,104,701,null,227,null,911]
    root3 = build_tree([236, 104, 701, None, 227, None, 911])
    print(sol.getMinimumDifference(root3))  # Expected: 9
