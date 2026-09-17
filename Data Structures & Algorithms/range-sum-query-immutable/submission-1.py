class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        total = 0

        for n in nums:
            total += n
            self.prefix_sum.append(total)
        
    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix_sum[right]
        left_sum = 0 if left == 0 else self.prefix_sum[left - 1]
        return right_sum - left_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)