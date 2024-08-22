"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        oldToNew = {}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToNew[cur] = copy
            cur = cur.next
            
        cur = head
        while cur:
            copy = oldToNew[cur]
            copy.next = oldToNew.get(cur.next)
            copy.random = oldToNew.get(cur.random)
            cur = cur.next 
        
        
        return oldToNew[head]