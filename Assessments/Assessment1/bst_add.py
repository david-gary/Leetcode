# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#countS[s[i]] = 1 + counts.get(s[i], 0)


class Solution:
    def findTarget(self, root: TreeNode, k) -> bool:
        needed = {}

        def traverse(root: TreeNode):
            if not root:
                return False
            else:
                complement = needed.get(root.val, None)
                if complement != None:
                    return True
                else:
                    needed[k - root.val] = True
                return traverse(root.left) or traverse(root.right)

        return traverse(root)
