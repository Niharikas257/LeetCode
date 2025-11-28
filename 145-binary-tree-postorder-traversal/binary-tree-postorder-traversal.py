# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:  
        # if not root:
        #     return []
        # res = []
        # stack = [root]
        # while stack:
        #     cur = stack.pop()
        #     res.append(cur.val)
        #     if cur.left:
        #         stack.append(cur.left)
        #     if cur.right:
        #         stack.append(cur.right)
            
        # return res[::-1]

        if not root:
            return []

        res = []
        stack = []
        cur = root
        visited = None

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                peek = stack[-1]
                if peek.right and visited != peek.right:
                    cur = peek.right
                else:
                    res.append(peek.val)
                    visited = stack.pop()
        return res        