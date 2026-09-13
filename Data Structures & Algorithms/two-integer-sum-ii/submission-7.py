class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if target - (numbers[r] + numbers[l]) > 0:
                l += 1
            elif target - (numbers[r] + numbers[l]) < 0:
                r -= 1
            else:
                break

        return [l + 1, r + 1]
