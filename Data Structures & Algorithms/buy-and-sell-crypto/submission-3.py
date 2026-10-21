class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, prof, greatest = 0, 0, 0, 0

        while r < len(prices):
            prof = prices[r] - prices[l]

            if prof > greatest:
                greatest = prof
        
            if prof < 0:
                l = r

            r+=1

        return greatest
        