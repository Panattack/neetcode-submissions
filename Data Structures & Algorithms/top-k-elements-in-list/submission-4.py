class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = Counter(nums)
        h = [(-count, num) for num, count in freq_count.items()]
        heapq.heapify(h)
        res = []

        for i in range(k):
            freq_num = heapq.heappop(h)
            res.append(freq_num[1])

        return res