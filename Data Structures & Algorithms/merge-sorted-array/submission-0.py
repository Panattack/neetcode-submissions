class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(n):
            j = m + i
            nums1[j] = nums2[i]
            while j > 0:
                if nums1[j - 1] > nums1[j]:
                    temp = nums1[j]
                    nums1[j] = nums1[j - 1]
                    nums1[j - 1] = temp
                    j -= 1
                else:
                    break
            