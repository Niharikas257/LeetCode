        # You can have all the passengers of next trip (considering the total capacity and remaining capacity) iff the pickup spot for next trip is farther than the drop off spot of previous trip.
        # so, we sort them based on pick up spot, and if the pick up of next is less than the drop off for first, we try to merge them iff capacity allows

from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        delta = {}

        for p, start, end in trips:
            delta[start] = delta.get(start, 0) + p
            delta[end] = delta.get(end, 0) - p

        curr = 0
        for x in sorted(delta.keys()):
            curr += delta[x]
            if curr > capacity:
                return False

        return True
