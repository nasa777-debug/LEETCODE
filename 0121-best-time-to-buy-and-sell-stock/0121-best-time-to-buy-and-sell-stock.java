class Solution {
    public int maxProfit(int[] prices) {
        int max_profit=0;
        int min_price=1000000;
        for(int i=0;i<prices.length;i++){
            if(min_price>prices[i]) min_price=prices[i];
            if(max_profit<(prices[i]-min_price))    max_profit=(prices[i]-min_price);
        }
        return max_profit;
    }
}