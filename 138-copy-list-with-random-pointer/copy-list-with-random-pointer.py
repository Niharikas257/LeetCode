"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         oldToCopy = {None: None}

#         cur = head
#         while cur:
#             copy = Node(cur.val)
#             oldToCopy[cur] = copy
#             cur = cur.next
#         cur = head
#         while cur:
#             copy = oldToCopy[cur]
#             copy.next = oldToCopy[cur.next]
#             copy.random = oldToCopy[cur.random]
#             cur = cur.next
#         return oldToCopy[head]
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 1) First pass: for each original node, insert its copy right after it.
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # 2) Second pass: assign random pointers for the copies.
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # 3) Third pass: unweave to restore original list and extract the copy.
        pseudo_head = Node(0)
        copy_tail = pseudo_head
        curr = head
        while curr:
            copy = curr.next
            # restore original .next
            curr.next = copy.next
            # append copy to the new list
            copy_tail.next = copy
            copy_tail = copy
            curr = curr.next

        return pseudo_head.next