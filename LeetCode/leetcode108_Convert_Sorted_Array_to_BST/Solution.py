class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if not nums:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


def tree_to_list(root):
    """Convert tree to level-order list for easy comparison"""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    sol = Solution()

    # Test 1: nums = [-10,-3,0,5,9]
    result1 = sol.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(tree_to_list(result1))  # Expected: [0,-3,9,-10,null,5] or [0,-10,5,null,-3,null,9]

    # Test 2: nums = [1,3]
    result2 = sol.sortedArrayToBST([1, 3])
    print(tree_to_list(result2))  # Expected: [3,1] or [1,null,3]

    # Test 3: nums = [1]
    result3 = sol.sortedArrayToBST([1])
    print(tree_to_list(result3))  # Expected: [1]
