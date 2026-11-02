class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        logged = math.log(n, 4)

        return logged == int(logged)
