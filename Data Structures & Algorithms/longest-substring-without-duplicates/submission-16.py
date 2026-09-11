class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        length, L = 0, 0

        for R in range(len(s)):
            if s[R] in window.keys():
                L = max(window[s[R]] + 1, L)
            window[s[R]] = R
            length = max(length, R - L + 1)

        return length
