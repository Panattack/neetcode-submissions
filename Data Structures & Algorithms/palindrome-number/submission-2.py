class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        num = x

        while num > 0:
            last_digit = num % 10
            rev = rev * 10 + last_digit
            num = num // 10

        return rev == x
