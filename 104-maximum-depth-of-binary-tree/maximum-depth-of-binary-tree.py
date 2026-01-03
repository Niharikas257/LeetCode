# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 1. let's do the inorder traversal, now because you need to add the depth, go to the root, go to the right and then add the depth again, so this basically means backtracking.
        # 2. The good part is, using stack will do that for you. When you pop the value from the stack, it is taking out that depth which you wanted to subtract while moving back to the root.
        stack = []
        cur = root
        depth = 0
        best = 0
        while stack or cur is not None:
            while cur:
                depth += 1
                stack.append([cur, depth])
                cur = cur.left
            cur, depth = stack.pop()
            best = max(best, depth)

            cur = cur.right
        return best
        # stack = []
        # cur = root
        # res = 0
        # depth = 0

        # while stack or cur is not None:
        #     while cur:
        #         depth += 1
        #         stack.append([cur, depth])
        #         cur = cur.left

        #     cur, depth = stack.pop()
        #     res = max(res, depth)
        #     cur = cur.right
        # return res


############### STACK##############
        # res = 0
        # stack = [[root, 1]]
        # if root is None:
        #     return 0

        # while stack:
        #     node, depth = stack.pop()
        #     res = max(res, depth)
        #     if node.left:
        #         stack.append([node.left, depth+1])
        #     if node.right:
        #         stack.append([node.right, depth + 1])
        # return res
###################################
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))







        