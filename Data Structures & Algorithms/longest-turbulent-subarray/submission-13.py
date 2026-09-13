from enum import Enum

class State(Enum):
    IDLE = -1
    EVEN = 0
    ODD = 1

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_length, current_length = 1, 0
        previous_state = State.IDLE
        L = 0
        R = 1

        while R < len(arr):
            if arr[R] > arr[R - 1] and previous_state != State.ODD:
                previous_state = State.ODD
                max_length = max(max_length, R - L + 1)
                R += 1
            elif arr[R] < arr[R - 1] and previous_state != State.EVEN:
                previous_state = State.EVEN
                max_length = max(max_length, R - L + 1)
                R += 1
            else:
                R = R + 1 if arr[R] == arr[R - 1] else R
                L = R - 1
                previous_state = State.IDLE
                
        return max_length
