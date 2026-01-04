"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
# from typing import List

# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         if root is None:
#             return []

#         res = []
#         stack = [root]

#         while stack:
#             node = stack.pop()
#             res.append(node.val)

#             # Push children in normal order
#             # so that after reversing res, the order becomes correct postorder.
#             if node.children:
#                 stack.extend(node.children)

#         # Reverse to convert "root-first" into "children-first"
#         res.reverse()
#         return res

from typing import List

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        res = []
        stack = [(root, False)]  # (node, expanded_flag)

        while stack:
            node, expanded = stack.pop()
            if node is None:
                continue
            if not expanded:
                stack.append((node, True))
                if node.children:
                    for child in reversed(node.children):
                        stack.append((child, False))
            else:
                res.append(node.val)
        return res

