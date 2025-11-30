# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if p is None and q is None:
        #     return True
        # if p and q and p.val == q.val:
        #     return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
        # else:
        #     return False
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        
        def bfs(node):
            res = []
            q = collections.deque()
            q.append(node)
            while q:
                cur = q.popleft()
                if cur is None:
                    res.append(None)
                    continue
                res.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.left is None:
                    q.append(None)
                if cur.right:
                    q.append(cur.right)
                if cur.right is None:
                    q.append(None)
                
            return res
        
        res_p = bfs(p)
        res_q = bfs(q)
        if res_p and res_q and res_p == res_q:
            return True
        else: 
            return False