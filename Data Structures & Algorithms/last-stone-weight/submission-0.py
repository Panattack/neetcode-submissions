class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * n for n in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -1 *heapq.heappop(stones)
            second = -1 * heapq.heappop(stones)
            res = first - second
            if res > 0:
                heapq.heappush(stones, -res)

        return -1 * stones[0] if len(stones) == 1 else 0
        