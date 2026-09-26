# # Implementation of QuickSort
# def quickSort(arr: list[int], s: int, e: int) -> list[int]:
#     if e - s + 1 <= 1:
#         return arr

#     pivot = arr[e]
#     left = s # pointer for left side

#     # Partition: elements smaller than pivot on left side
#     for i in range(s, e):
#         if arr[i] < pivot:
#             tmp = arr[left]
#             arr[left] = arr[i]
#             arr[i] = tmp
#             left += 1

#     # Move pivot in-between left & right sides
#     arr[e] = arr[left]
#     arr[left] = pivot
    
#     # Quick sort left side
#     quickSort(arr, s, left - 1)

#     # Quick sort right side
#     quickSort(arr, left + 1, e)

#     return arr

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean_distance = lambda x: x[0]**2 + x[1]**2

        def partition(l, r):
            pivotIdx = r
            pivotDistance = euclidean_distance(points[pivotIdx])
            left = l

            for i in range(l, r):
                if euclidean_distance(points[i]) <= pivotDistance:
                    points[i], points[left] = points[left], points[i]
                    left += 1
            
            points[pivotIdx], points[left] = points[left], points[pivotIdx]

            return left

        L, R = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L, R)
            if pivot > k:
                R = pivot - 1
            else:
                L = pivot + 1
        return points[:k]
