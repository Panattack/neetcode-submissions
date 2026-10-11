class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean_distance = lambda x: x[0]**2 + x[1]**2

        distance_map = defaultdict(list)

        for x in points:
            distance_map[euclidean_distance(x)].append(x)

        distances = list(distance_map.keys())

        heapq.heapify(distances)
        k_points = []
        remaining_points = 0
        last_distance = 0

        for i in range(k):
            if remaining_points > 0:
                remaining_points -= 1
                k_points.append(distance_map[last_distance].pop())
            else:
                min_distance = heapq.heappop(distances)
                k_points.append(distance_map[min_distance].pop())
                remaining_points = len(distance_map[min_distance])
                if remaining_points > 0:
                    last_distance = min_distance

        return k_points
