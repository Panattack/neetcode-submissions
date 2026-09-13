from enum import Enum

class State(Enum):
    UP = 1
    DOWN = -1
    IDLE = 0

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_length, current_length = 1, 0
        previous_state = State.IDLE
        L = 0
        R = 1

        while R < len(arr):
            if arr[R] > arr[R - 1] and previous_state != State.UP:
                previous_state = State.UP
                max_length = max(max_length, R - L + 1)
                R += 1
            elif arr[R] < arr[R - 1] and previous_state != State.DOWN:
                previous_state = State.DOWN
                max_length = max(max_length, R - L + 1)
                R += 1
            else:
                R = R + 1 if arr[R] == arr[R - 1] else R
                L = R - 1
                previous_state = State.IDLE
                
        return max_length
