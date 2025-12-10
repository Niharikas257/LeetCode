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
        # stack = []
        # cur = root
        # visited = None

        # while cur or stack:
        #     if cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     else:
        #         peek = stack[-1]
        #         if peek.right and visited != peek.right:
        #             cur = peek.right
        #         else:
        #             res.append(peek.val)
        #             visited = stack.pop()
        # return res

        stack = []
        cur = root
        res = []
        visited = None

        if not root:
            return []

        while stack or cur:
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




