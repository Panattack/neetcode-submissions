class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = [0] * n
        suffix_max = [0] * n
        max_left, max_right = 0, 0

        for i in range(n):
            if height[i] > max_left :
                max_left = height[i]
            if height[n - 1 - i] > max_right:
                max_right = height[n - 1 - i]
            prefix_max[i] = max_left
            suffix_max[n - 1 - i] = max_right

        res = 0
        for i in range(n):
            water = (min(prefix_max[i], suffix_max[i]) - height[i])
            res += water
            
        return res

