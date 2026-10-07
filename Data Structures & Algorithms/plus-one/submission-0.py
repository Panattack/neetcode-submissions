class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = deque(digits)
        increment = True
        i = len(digits) - 1
        while increment and i >= 0:
            if digits[i] != 9:
                increment = False
                digits[i] += 1
            else:
                digits[i] = 0
            i -= 1
        
        if increment:
            digits.appendleft(1)

        return list(digits)                
