# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
       
        
        # Create 2 dummy nodes
        ldummy = ListNode(0)
        rdummy = ListNode(0)
        
        # create 2 pointers for these 2 newly created lists and they initially point to the starting of the new lis
        lpointer = ldummy
        rpointer = rdummy
        
        while head:
            if head.val<x:
                lpointer.next = head
                lpointer = lpointer.next
            else:
                rpointer.next = head
                rpointer = rpointer.next
            head = head.next
            
        lpointer.next = rdummy.next
        rpointer.next = None
        return ldummy.next
  
            
        
        