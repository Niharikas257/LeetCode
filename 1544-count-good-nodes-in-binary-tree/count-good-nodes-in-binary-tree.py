# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # if not root:
        #     return 0
        # stack = [(root, root.val)]
        # good =  []
        # max_so_far = root.val


        # while stack:
        #     cur, max_so_far = stack.pop()
        #     if cur.val >= max_so_far:
        #         good.append(cur.val)
        #     max_so_far = max(max_so_far, cur.val)
        #     if cur.left:
        #         stack.append((cur.left, max_so_far))
        #     if cur.right:
        #         stack.append((cur.right, max_so_far))
        # # print (good)
        # return len(good)

        if not root:
            return 0
        stack = [(root, root.val)]
    
        good = []
        max_so_far = root.val
        while stack:
            cur, max_so_far = stack.pop()
            if cur.val >= max_so_far:
                good.append(cur.val)
            max_so_far = max(max_so_far, cur.val)
            if cur.left:
                stack.append((cur.left, max_so_far))
            if cur.right:
                stack.append((cur.right, max_so_far))
        return len(good)

        # def dfs(node, max_val):
        #     if not node:
        #         return 0
        #     res = 1 if node.val >= max_val else 0

        #     max_val = max(max_val, node.val)
        #     res += dfs(node.right, max_val)
        #     res += dfs(node.left, max_val)
        #     return res
        
        # return dfs(root, root.val)
        




