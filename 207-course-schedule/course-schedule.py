class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course,pre in prerequisites:
            graph[pre].append(course)
            
        indegree = [0] * numCourses
        for pre in range(numCourses):
            for course in graph[pre]:
                indegree[course] += 1


        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        order = []
        while q:
            course = q.popleft()
            order.append(course)
            for next_course in graph[course]:
                indegree[next_course]-=1
                if indegree[next_course] == 0:
                    q.append(next_course)
        return True if len(order) == len(indegree) else False
