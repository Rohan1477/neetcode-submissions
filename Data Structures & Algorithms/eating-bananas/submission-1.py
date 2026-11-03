class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = piles[0]

        for i in range(len(piles)):
            maxPile = max(maxPile, piles[i])

        def testK(k):

            hCount = 0

            for i in range(len(piles)):
                currPile = piles[i]
                hCount += math.ceil(currPile/k)

            if hCount <= h:
                return True
            return False
        
        low, high = 1, maxPile
        
        while low <= high:
            mid = (low + high) // 2
            if testK(mid):
                ans = mid
                high = mid -1
            
            else:
                low = mid +1
        
        return ans
        

