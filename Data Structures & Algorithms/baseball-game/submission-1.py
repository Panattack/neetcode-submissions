class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = list()

        for oper in operations:
            if oper == '+':
                records.append(records[-1] + records[-2])
            elif oper == 'D':
                records.append(records[-1] * 2)
            elif oper == 'C':
                records.pop(-1)
            else:
                records.append(int(oper))
        
        return sum(records)