"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # if not root:
        #     return []
        # stack = [root]
        # res = []
        # while stack:
        #     cur = stack.pop()
        #     res.append(cur.val)
        #     if cur.children:
        #         for child in reversed(cur.children):
        #             # if child is not None:
        #             stack.append(child)
        # return res

        res = []
        def dfs(node):
            if not node:
                return []
            res.append(node.val)
            for child in node.children:
                dfs(child)
            # return res
        dfs(root)
        return res
