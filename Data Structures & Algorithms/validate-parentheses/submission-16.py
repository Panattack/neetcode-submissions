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
            elif ch in closedTabs.keys():
                if not stack:
                    return False
                openTab = stack.pop()

                if openTab != closedTabs[ch]:
                    return False

        return len(stack) == 0
