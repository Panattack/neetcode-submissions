class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 1
        majority_el = nums[0]

        for n in nums[1:]:
            if counter == 0:
                counter = 1
                majority_el = n
            else:
                if majority_el != n:
                    counter -= 1
                else:
                    counter += 1
        return majority_el
        