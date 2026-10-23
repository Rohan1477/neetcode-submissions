class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        highest = 0

        while r < len(prices):
            curr = prices[r] - prices[l]

            highest = max(curr, highest)

            if curr < 0:
                l=r
            r+=1
        return highest