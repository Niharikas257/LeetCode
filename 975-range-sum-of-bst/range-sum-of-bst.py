# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        total = 0
        while stack:
            cur = stack.pop()
            if cur is None:
                continue
            if cur.val < low:
                stack.append(cur.right)
            elif cur.val > high:
                stack.append(cur.left)
            else:
                total += cur.val
                stack.append(cur.left)
                stack.append(cur.right)
        return total
