class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_table = dict()
        L = 0
        max_length = 0
        max_char_freq = 0

        for R in range(len(s)):
            if not(s[R] in hash_table.keys()):
                hash_table[s[R]] = 0

            hash_table[s[R]] += 1
            max_char_freq = max(max_char_freq, hash_table[s[R]])

            while (R - L + 1) - max_char_freq > k:
                hash_table[s[L]] -= 1
                L += 1

            max_length = max(max_length, R - L + 1)
        
        return max_length
