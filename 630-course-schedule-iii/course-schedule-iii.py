class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # 1. Sort on the basis of lastDay, because if something will end early, you will have more time in your hands.
        # 2. Now, you do not need heap to choose which one to take, you simply take the one with less finish time, but you will need heap when you will not be able to finish a task with t time before the lastDay, in that case you would need something to get you the course which will end before that date.
        # 3. Heap can help when you are not able to fit the courses which you have picked based on the sorting. When that state comes, you would want to delete the time which took the maximum time, which will be saved by the maxheap.
        # 4. This is required here because we have to be greedy about both the lastday and duration also.

        # Edge case - 1. if duration > lastDay: not possible

        # courses = [(duration, lastDay, i) for i in range(len(courses))]
        courses.sort(key=lambda x:x[1])

        maxheap = []
        current_day = 0
        for duration, lastday in courses:
            current_day += duration
            heapq.heappush(maxheap, -duration)

            if current_day > lastday:
                current_day += heapq.heappop(maxheap)
        return len(maxheap)
