# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if not root or not p or not q:
        #     return False
        
        # if (max(p.val, q.val) < root.val):
        #     return self.lowestCommonAncestor(root.left, p, q)
        # if (min(p.val, q.val) > root.val):
        #     return self.lowestCommonAncestor(root.right, p, q)
        # return root
        cur = root

        while cur:
            if p.val>cur.val and q.val>cur.val:
                cur = cur.right
            elif p.val<cur.val and q.val<cur.val:
                cur = cur.left
            else:
                return cur
        
        