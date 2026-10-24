class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1) - 1, len(text2) - 1
        def dfs(i, j, cache):
            if i > len1 or j > len2:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
        
            if text1[i] == text2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1, cache) + 1
            else:
                cache[(i, j)] = max(dfs(i + 1, j, cache), dfs(i, j + 1, cache))
            return cache[(i, j)]
        
        cache = {}
        return dfs(0, 0, cache)
