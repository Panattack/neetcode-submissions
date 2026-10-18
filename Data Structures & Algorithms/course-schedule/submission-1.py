class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)

        visiting = set()

        def dfs(visiting, graph, a):
            if a in visiting:
                # Cycle detected
                return False
            if not graph[a]:
                # Already processed
                return True

            visiting.add(a)

            for v in graph[a]:
                if not dfs(visiting, graph, v):
                    return False
            
            visiting.remove(a)
            graph[a] = []

            return True

        for a in graph:
            if not dfs(visiting, graph, a):
                return False
        
        return True
