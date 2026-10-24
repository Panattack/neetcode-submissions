class Solution:
    def countBits(self, n: int) -> List[int]:
        ls = []

        for i in range(n + 1):
            ls.append(bin(i).count('1'))

        return ls
    