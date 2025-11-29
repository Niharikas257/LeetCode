# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        col_map = defaultdict(list)
        # q = deque([(root, 0, 0)])
        stack = ([(root, 0,0)])
        cur = 0
        # while q:
        while stack:
            # cur, row, col = q.popleft()
            cur, row, col = stack.pop()
            # col_map[col].append((row, cur.val))
            col_map[col].append((row, cur.val))
            if cur.left:
                # q.append((cur.left, row+1, col -1))
                stack.append((cur.left, row+1, col -1))
            if cur.right:
                # q.append((cur.right, row+1, col+1))
                stack.append((cur.right, row+1, col+1))
        
        result = []
        for col in sorted(col_map.keys()):
            col_map[col].sort()
            result.append([val for row, val in col_map[col]])
        return result
