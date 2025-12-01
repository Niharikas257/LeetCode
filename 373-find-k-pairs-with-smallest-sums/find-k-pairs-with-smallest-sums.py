class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minheap = [(nums1[0] + nums2[0], 0, 0)] # -> sum of the first 2 values from both the arrays, and indices
        visited = set((0,0))
        res = []

        while minheap and len(res)<k:
            _, i, j = heapq.heappop(minheap)
            res.append((nums1[i],nums2[j]))
            if i+1 < len(nums1) and (i+1, j) not in visited:
                visited.add((i+1, j))
                heapq.heappush(minheap, ((nums1[i+1] + nums2[j]), i+1, j))
            if j+1 < len(nums2) and (i, j+1) not in visited:
                visited.add((i, j+1))
                heapq.heappush(minheap, ((nums1[i] + nums2[j+1]), i, j+1))
            
        return res
            
        