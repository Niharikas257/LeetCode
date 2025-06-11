# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr = head

        while curr:
            # if curr.val not in visited:
            #     visited.append(curr.val)
            
            if curr in visited:
                return True
            visited.add(curr)
            curr= curr.next
        return False

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         visited = set()      # 1) use a set of nodes, not a list of values
#         curr = head

#         while curr:
#             if curr in visited:   # 2) if we’ve seen this node before, there’s a cycle
#                 return True
#             visited.add(curr)     # 3) mark the current node as seen
#             curr = curr.next      # 4) advance
#         return False              # no cycle found

        