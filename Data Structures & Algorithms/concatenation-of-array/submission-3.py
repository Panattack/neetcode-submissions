class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * 2 * length

        for index, num in enumerate(nums):
            ans[index] = num
            ans[index + length] = num

        return ans