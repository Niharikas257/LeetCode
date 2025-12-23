class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 0
        q = deque()
        if len(nums) < k:
            return []
        if not nums or k == 0:
            return []
        res = []

        for right in range(len(nums)):
            while q and q[0] <= right-k:
                q.popleft()
            while q and nums[q[-1]] <= nums[right]:
                q.pop()
            q.append(right)
            if right >= k-1:
                res.append(nums[q[0]])
        return res
            





       
        