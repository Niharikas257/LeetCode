# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # q = collections.deque()
        # q.append(root)

        # while q:
        #     rightmost = None

        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node:
        #             rightmost = node
        #             q.append(node.left)
        #             q.append(node.right)
        #     if rightmost: # This loop will run only after the previous loop len(q) number of times, len(q) is the number of elements in that level.  So, once the previous loop runs the number of times = number of elements in the level, only then this loop will run and by then the rightmost element has already been updated to the last value (right most) value in the level.
        #         res.append(rightmost.val)
        # return res
        res = []

        def dfs(node,depth):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val)
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        dfs(root,0)
        return res

        