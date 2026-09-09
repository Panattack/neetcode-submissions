class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = list()
        total = 0
        for oper in operations:
            if oper == '+':
                twoSum = records[-1] + records[-2]
                records.append(twoSum)
                total += twoSum
            elif oper == 'D':
                doubleRecord = records[-1] * 2
                records.append(doubleRecord)
                total += doubleRecord
            elif oper == 'C':
                lastRecord = records[-1]
                records.pop(-1)
                total -= lastRecord
            else:
                total += int(oper)
                records.append(int(oper))
        
        return sum(records)