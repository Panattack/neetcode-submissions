class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map_mag = Counter(magazine)
        map_ransom = Counter(ransomNote)

        for n in map_mag:
            if n in map_ransom:
                if map_mag[n] < map_ransom[n]:
                    return False
                map_ransom.pop(n)
        
        return not bool(len(map_ransom))
