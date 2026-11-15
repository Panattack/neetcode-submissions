class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_map = {i: 0 for i in range(1, n + 1)}

        for x in nums:
            num_map[x] += 1
        
        return [i for i in range(1, n + 1) if num_map[i] == 0]

