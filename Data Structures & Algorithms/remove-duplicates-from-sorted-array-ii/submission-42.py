class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)

        while r < n:
            print(l, r, nums)
            nums[l] = nums[r]
            if r + 1 < n and nums[r + 1] == nums[r]:
                l += 1
                r += 1
                nums[l] = nums[r]
            while r < n and nums[l] == nums[r]:
                r += 1
            l += 1

        return l
