# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
#         stack = []
#         cur = root
#         # res = []
#         prev = None

#         while stack or cur:
#             while cur:
#                 stack.append(cur)
#                 cur = cur.left
            
#             cur = stack.pop()
#             if prev is not None and cur.val <= prev:
#                 return False
#             prev = cur.val

#             cur = cur.right
#         return True

        # for i in range(1, len(res)):
        #     if res[i] <= res[i-1]:
        #         return False
        
        # return True

        # return True if res = res.sorted() else False

        # 1. a valid binary search tree has sorted output
        # 2. we are given breadth first search
        # 3. 