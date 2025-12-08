class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        n = len(s)

        max_count = max(freq.values())
        if max_count > (n+1)//2:
            return ""
        
        # heap = [(-count, char) for count, char in freq.items()]
        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)

        result = []

        while len(heap) > 1:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)

            result.append(char1)
            result.append(char2)

            if count1 + 1< 0:
                heapq.heappush(heap, (count1 + 1, char1))
            
            if count2 + 1< 0:
                heapq.heappush(heap, (count2 + 1, char2))

        if heap:
            count, char = heapq.heappop(heap)

            if result and result[-1] == char:
                return ""
            result.append(char)

        return "".join(result)
        