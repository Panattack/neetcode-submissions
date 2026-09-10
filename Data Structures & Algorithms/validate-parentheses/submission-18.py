class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedTabs = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        for ch in s:
            if ch in closedTabs.values():
                stack.append(ch)
            elif stack and closedTabs[ch] == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
