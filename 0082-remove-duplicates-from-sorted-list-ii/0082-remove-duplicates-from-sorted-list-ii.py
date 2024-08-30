# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
            
            else:
                prev = cur
            cur = cur.next
        
        return dummy.next
    
                    
        