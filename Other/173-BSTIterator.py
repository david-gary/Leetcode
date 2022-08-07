# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root):
        self.stack = []
        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left

    def next(self) -> int:
        if self.stack:
            new = self.stack.pop()
            curr_node = new
            if curr_node.right:
                curr_node = curr_node.right
            else:
                curr_node = None
            while curr_node:
                self.stack.append(curr_node)
                curr_node = curr_node.left
            return curr_node.val
        else:
            return None

    def hasNext(self) -> bool:
        return self.stack != []
