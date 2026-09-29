class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in index_map.keys():
                return [index_map[diff], i]
            index_map[nums[i]] = i
        