class Solution {
    public int maxProfit(int[] prices) {
        int maxprofit=0;
        int min_price=1000000;
        for(int i=0;i<prices.length;i++){
            min_price=Math.min(min_price,prices[i]);
            maxprofit=Math.max(maxprofit,prices[i]-min_price);
        }
        return maxprofit;
    }
}