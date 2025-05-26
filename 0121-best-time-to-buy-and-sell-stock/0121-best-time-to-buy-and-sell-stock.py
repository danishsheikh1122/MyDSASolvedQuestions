class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        # """
        # max_profit=0
        # ptr=0
        # i=1
        # temp=i
        # while ptr<len(prices):
        #     res=prices[ptr]-prices[i]
        #     max_profit=max(max_profit,res)
        #     if i==len(prices)-1:
        #         temp+=1
        #         i=temp
        #     i+=1
        #     ptr+=1
        # if max_profit<0:
        #     return 0
        # return max_profit
        # greg hog approach
        max_profit=0
        min_price=float('inf')
        for current_val in prices:
            if current_val<min_price:
                min_price=current_val
            
            profit = current_val-min_price

            max_profit=max(profit,max_profit)

        return max_profit














