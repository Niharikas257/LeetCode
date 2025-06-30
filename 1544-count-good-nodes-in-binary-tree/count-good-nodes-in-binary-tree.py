# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, root.val)]
        good = []
        while stack:
            node, max_so_far = stack.pop()

            if node.val >= max_so_far:
                good.append(node.val)
            new_max = max(max_so_far, node.val)

            if node.right:
                stack.append((node.right, new_max))
                

            if node.left:
                stack.append((node.left, new_max))
                
            
        return len(good)


