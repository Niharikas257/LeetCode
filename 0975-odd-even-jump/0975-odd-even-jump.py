class Solution(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 1:
            return 1
        
        odd = [False]*n
        even = [False]*n
        
        odd[-1] = even[-1] = True
        
        next_odd = [None]*n
        next_even = [None]*n
        
        sorted_idx = sorted(range(n), key = lambda i:(arr[i], i))
        def make_monotonic_stack(indices):
            result = [None]*n
            stack = []
            for i in indices:
                while stack and stack[-1] < i:
                    result[stack.pop()] = i
                stack.append(i)
            return result
        
        
        next_odd = make_monotonic_stack(sorted_idx)
        
        sorted_idx = sorted(range(n), key = lambda i:(-arr[i], i))
        next_even = make_monotonic_stack(sorted_idx)
        
        for i in range(n - 2, -1, -1):
            if next_odd[i] is not None:
                odd[i] = even[next_odd[i]]
            if next_even[i] is not None:
                even[i] = odd[next_even[i]]
                
            
        return sum(odd)
        
        
        
        
            