# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # q=deque()
        q = deque([(root, 1)])
        while q:
            cur, d = q.popleft()
            if cur.left is None and cur.right is None:
                return d
            if cur.left is not None:
                q.append((cur.left, d+1))
            if cur.right is not None:
                q.append((cur.right, d+1))


