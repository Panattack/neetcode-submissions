class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = res = 0
        prefix_sums = {0: 1}

        for num in nums:
            # for each position, we want to count how many earlier positions
            # have a prefix sum equal to currentPrefixSum - k
            cur_sum += num
            diff = cur_sum - k
            
            # counts subarrays ending here with sum k
            res += prefix_sums.get(diff, 0)
            prefix_sums[cur_sum] = 1 + prefix_sums.get(cur_sum, 0)
        
        return res
