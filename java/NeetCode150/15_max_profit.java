class Solution 
{
    public int maxProfit(int[] prices) 
    {
        int l = 0;
        int r;
        int max_prof = 0;
        if(prices.length < 2) return max_prof; // Can't be a profit if there is only 1 entry.
        
        while(l+1 < prices.length && prices[l+1] < prices[l]) l += 1;
        
        r = l + 1;
        while(r < prices.length)
        {
            max_prof = Math.max(max_prof, prices[r]-prices[l]);
            if(prices[r] < prices[l]) l = r;
            r += 1;
        }
        return max_prof;
    }
}
