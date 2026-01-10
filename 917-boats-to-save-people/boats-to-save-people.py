class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        groups= 0
        while left <= right:
            if left < right and people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            
            groups += 1
        return groups
        