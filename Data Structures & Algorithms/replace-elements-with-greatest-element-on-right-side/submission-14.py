class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newList = [0] * len(arr)
        newList[len(arr) - 1] = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            newList[i] = max(arr[i + 1], newList[i + 1])

        newList[-1] = -1
        
        return newList