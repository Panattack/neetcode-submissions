class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = [0] * len(code)
        for i in range(len(code)):
            for step in range(1, abs(k) + 1):
                res[i] += code[(i + (step if k > 0 else - step)) % len(code)]
        return res
