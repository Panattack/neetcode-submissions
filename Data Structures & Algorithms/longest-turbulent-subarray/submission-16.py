from enum import Enum

class State(Enum):
    DOWN = -1
    IDLE = 0
    UP = 1

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_length, current_length = 0, 0
        current_state = State.IDLE

        for R in range(len(arr) - 1):
            if arr[R] > arr[R + 1]:
                current_length = current_length + 1 if current_state == State.DOWN else 1
                current_state = State.UP
            elif arr[R] < arr[R + 1]:
                current_length = current_length + 1 if current_state == State.UP else 1
                current_state = State.DOWN
            else:
                current_state = State.IDLE
                current_length = 0
            
            max_length = max(max_length, current_length)
                
        return max_length + 1 
