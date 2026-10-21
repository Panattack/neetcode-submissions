class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {ch : 0 for ch in s}

        for ch in s:
            counter[ch] += 1
        
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        
        return -1