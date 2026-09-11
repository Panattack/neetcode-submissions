class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        sum_k = 0
        counter = 0
        target = k * threshold

        for R in range(len(arr)):
            sum_k += arr[R]
            if R - L + 1 == k:
                if sum_k >= target:
                    counter += 1
                sum_k -= arr[L]
                L += 1

        return counter
