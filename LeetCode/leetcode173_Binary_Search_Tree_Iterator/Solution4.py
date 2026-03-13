from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.vals = []
        self.getVals(root)
        self.current = 0

    def next(self) -> int:
        result = None
        if self.hasNext():
            result = self.vals[self.current]
            self.current += 1
        return result

    def hasNext(self) -> bool:
        return self.current < len(self.vals)

    def getVals(self, root):
        if not root:
            return
        self.getVals(root.left)
        self.vals.append(root.val)
        self.getVals(root.right)

if __name__ == "__main__":
    def build(vals):
        if not vals:
            return None
        nodes = [TreeNode(v) if v is not None else None for v in vals]
        for i in range(len(nodes)):
            if nodes[i]:
                l, r = 2*i+1, 2*i+2
                if l < len(nodes): nodes[i].left = nodes[l]
                if r < len(nodes): nodes[i].right = nodes[r]
        return nodes[0]

    # Tree: [7, 3, 15, null, null, 9, 20]
    root = build([7, 3, 15, None, None, 9, 20])
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
