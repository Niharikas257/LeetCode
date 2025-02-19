class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = [i for i in range(n)]
        used = []
        count = [0] * n

        for start,end in meetings:
            # This is just freeing up the used room
            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            # This code will decide where the next meeting will go based on the used and available rooms.
            # If the room is not available
            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + (end-start)
                heapq.heappush(available, room)

            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1

        return count.index(max(count))


            