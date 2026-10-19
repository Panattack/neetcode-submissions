class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for src, dst in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        finish = 0
        while queue:
            i = queue.popleft()
            finish += 1
            for j in adj[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
        
        return finish == numCourses                
