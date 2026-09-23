class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_dict = {}

        for c in s:
            if c not in hash_dict:
                hash_dict[c] = 0
            hash_dict[c] += 1
        
        for c in t:
            if c not in hash_dict:
                return False
            else:
                if hash_dict[c] == 0:
                    return False
                hash_dict[c] -= 1
        
        return True
