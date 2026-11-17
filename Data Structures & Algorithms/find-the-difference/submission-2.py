class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash_s = Counter([c for c in s])
        hash_t = Counter([c for c in t])
        
        for c in t:
            if c not in hash_s or hash_s[c] != hash_t[c]:
                return c
