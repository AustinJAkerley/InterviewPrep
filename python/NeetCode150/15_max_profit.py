class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        wsb_max = 0
        l = 0
        while l < len(prices) - 1 and prices[l] > prices[l+1]:
            l+=1
        # l is low
        # look for high
        r = l + 1
        while r < len(prices): # Calculate new max diff
            wsb_max = max(wsb_max, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r = r + 1
        return wsb_max
