class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def hasPathSum(root, targetSum) -> bool:
    if root == None:
        return 0

    def pathSumSub(node, target):
        if node == None:
            return 0

        return (1 if (target - node.data) == 0 else 0) + pathSumSub(node.left, target - node.data) + pathSumSub(node.right, target - node.data)

    return hasPathSum(root.left, targetSum) + hasPathSum(root.right, targetSum) + hasPathSum(root, targetSum)




