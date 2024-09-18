class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        prefix= [0] * (n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1] # the prefix starts at 0 for first element
        
        dq = deque() # Initializes the dequeue
        min_len = float('inf') # Inititalizes the mininum length from infinity
        
        for i in range(n+1): # Runs the loop for the entire length of the array
            while dq and prefix[i] < prefix[dq[-1]]:
                dq.pop()
                
            while dq and prefix[i] - prefix[dq[0]] >= k:
                min_len = min(min_len, i-dq.popleft())
                
            dq.append(i)
        
        return min_len if min_len != float('inf') else -1
        