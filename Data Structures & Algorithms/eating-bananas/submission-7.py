class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = l + (r - l) // 2
            hoursToBeEaten = self.findEatingHours(mid, piles)
            if hoursToBeEaten > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        
        return res
            
    def findEatingHours(self, ratio, piles):
        hoursToBeEaten = sum([math.ceil(pile / ratio) for pile in piles])
        return hoursToBeEaten
