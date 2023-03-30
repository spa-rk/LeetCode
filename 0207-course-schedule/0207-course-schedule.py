class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0] * numCourses
        q = deque()
        toTake = []
        graph = defaultdict(list)
        
        for i, j in prerequisites:
            indegree[i] += 1
            graph[j].append(i)
        
        for k in range(numCourses):
            if indegree[k] == 0:
                q.appendleft(k)
        
        while q:
            curr = q.popleft()
            toTake.append(curr)
            for i in graph[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        return len(toTake) == numCourses