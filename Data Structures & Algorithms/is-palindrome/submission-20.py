class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            while L < R and not self.isAlphanumerical(s[L]):
                L += 1
            while L < R and not self.isAlphanumerical(s[R]):
                R -= 1
            if s[R].lower() != s[L].lower():
                return False
            R -= 1
            L += 1
        
        return True
    
    def isAlphanumerical(self, c):
        return (
            ord('a') <= ord(c) <= ord('z')
            or ord('A') <= ord(c) <= ord('Z')
            or ord('0') <= ord(c) <= ord('9')
        )
