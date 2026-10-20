class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        char_map = {i: chr(ord('A') + i) for i in range(26)}
        queue = deque()

        while columnNumber:
            columnNumber -= 1
            charLeft = columnNumber % 26
            queue.appendleft(charLeft)
            columnNumber //= 26

        return ''.join(char_map[char] for char in queue)
