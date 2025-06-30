# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        visited.sort(key=lambda x: x.val)  # Sort based on node values
        return visited[k - 1].val

        


            
        