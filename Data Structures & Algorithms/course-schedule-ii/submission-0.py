class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            indegrees[course] += 1
            graph[prereq].append(course)
        
        q = deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                q.append(course)

        res = []
        processed = 0
        while q:
            prereq = q.popleft()
            res.append(prereq)
            processed += 1
            for course in graph[prereq]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    q.append(course)

        return res if processed == numCourses else []