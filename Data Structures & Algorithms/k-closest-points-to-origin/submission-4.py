class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean_distance = lambda x: x[0]**2 + x[1]**2

        distance_map = defaultdict(list)

        for x in points:
            distance_map[euclidean_distance(x)].append(x)

        distances = list(distance_map.keys())

        heapq.heapify(distances)
        print(distance_map)
        k_points = []

        for i in range(k):
            min_distance = heapq.heappop(distances)
            k_points.append(distance_map[min_distance].pop())
            if len(distance_map[min_distance]) > 0:
                heapq.heappush(distances, min_distance)

        print(k_points)    
        return k_points
