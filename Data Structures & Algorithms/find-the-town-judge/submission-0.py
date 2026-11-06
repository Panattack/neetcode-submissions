class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_map = defaultdict(int)

        for ai, bi in trust:
            trust_map[ai] -= 1
            trust_map[bi] += 1
        
        for i in range(1, n + 1):
            if trust_map[i] == n - 1:
                return i
        
        return -1