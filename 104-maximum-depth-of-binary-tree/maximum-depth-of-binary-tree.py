# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root is None:
        #     return 0
        # q = deque([(root, 1)])
        # res = 0
        # while q:
        #     node, depth = q.popleft()
        #     res = max(res, depth)
        #     if node.left:
        #         q.append((node.left, depth+1))
        #     if node.right:
        #         q.append((node.right, depth+1))
        # return res

        stack = [([root, 1])]
        res = 0
        if not root:
            return 0

        while stack:
            cur, depth = stack.pop()
            res = max(res, depth)
            if cur.left:
                stack.append([cur.left, depth+1])
            if cur.right:
                stack.append([cur.right, depth + 1])
        return res            



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







        