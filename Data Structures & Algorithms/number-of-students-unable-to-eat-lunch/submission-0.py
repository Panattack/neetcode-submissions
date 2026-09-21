class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stud_dict = {0: 0, 1: 0}

        for i in range(len(students)):
            stud_dict[students[i]] += 1

        while sandwiches:
            avail_sandwich = sandwiches[0]
            if stud_dict[avail_sandwich] >= 1:
                sandwiches.pop(0)
                stud_dict[avail_sandwich] -= 1
            else:
                break

        return len(sandwiches)
                