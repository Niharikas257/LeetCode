class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(w/q, q) for q, w in zip(quality, wage)])
        
        min_cost = float('inf')
        quality_sum = 0
        max_heap = []
        
        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            quality_sum += q
            
            if len(max_heap) > k:
                quality_sum += heapq.heappop(max_heap)
                
            if len(max_heap) == k:
                min_cost = min(min_cost, ratio* quality_sum)
                
        return min_cost
        
        