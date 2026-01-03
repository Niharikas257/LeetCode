# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return False
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, q,p)
        if min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, q,p)
        return root
