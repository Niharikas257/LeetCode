# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n>0 and right:
            right = right.next
            n-=1
            
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        
        return dummy.next
        
            
#         length = 0
#         current = head
#         while current:
#             length += 1
#             current = current.next
        
#         pos_from_start = length-n
        
#         if pos_from_start == 0:
#             return head.next
        
#         current = head
#         for _ in range(pos_from_start-1):
#             current = current.next
            
#         current.next = current.next.next
        
#         return head


