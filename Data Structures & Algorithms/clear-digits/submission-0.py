class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for ch in s:
            if ord(ch) >= ord("a") and ord(ch) <= ord("z"):
                stack.append(ch)
            else:
                stack.pop(-1)

        return ''.join(stack)
