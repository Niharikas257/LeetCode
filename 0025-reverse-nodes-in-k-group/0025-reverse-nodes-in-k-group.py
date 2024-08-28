# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Initializations
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while True:
            kthnode = self.get_kth_node(prev_group_end, k)
            if not kthnode:
                break
            
            groupstart = prev_group_end.next
            nextgroupstart = kthnode.next
            
            prev, curr = kthnode.next, groupstart
            while curr != nextgroupstart:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            prev_group_end.next = prev
            groupstart.next = nextgroupstart
            prev_group_end = groupstart
        
        return dummy.next  # This should be outside the loop
    
    def get_kth_node(self, start, k):
        """
        :type start: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr = start
        while curr and k > 0:
            curr = curr.next
            k -= 1  # Fixed syntax error
        return curr
