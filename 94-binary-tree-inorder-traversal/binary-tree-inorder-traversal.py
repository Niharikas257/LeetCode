# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        if not root:
            return []
        cur= root

        while cur is not None or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            res.append(cur.val)

            cur = cur.right
        return res
