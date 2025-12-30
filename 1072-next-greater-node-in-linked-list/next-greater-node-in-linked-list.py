# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next

        ans = [0] * len(nums)  

        stack = []

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                ans[index] = nums[i]
            stack.append(i)
        return ans     