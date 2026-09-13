from enum import Enum

class State(Enum):
    IDLE = -1
    EVEN = 0
    ODD = 1

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_length, current_length = 0, 0
        current_state = State.IDLE

        for R in range(len(arr) - 1):
            if arr[R] > arr[R + 1]:
                current_length = current_length + 1 if current_state == State.ODD else 1
                current_state = State.EVEN
            elif arr[R] < arr[R + 1]:
                current_length = current_length + 1 if current_state == State.EVEN else 1
                current_state = State.ODD
            else:
                current_state = State.IDLE
                current_state = 0
            
            max_length = max(max_length, current_length)
                
        return max_length + 1        
