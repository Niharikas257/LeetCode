"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

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
            if expanded == False:
                stack.append((node, True))
                if node.children:
                    for child in reversed(node.children):
                        stack.append((child, False))
            else:
                res.append(node.val)
        return res

