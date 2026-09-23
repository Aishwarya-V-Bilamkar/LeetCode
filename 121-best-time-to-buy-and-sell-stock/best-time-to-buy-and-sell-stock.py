class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi=prices[0]
        ma=0
        for i in range(1,len(prices)):
            if prices[i]< mi:
                mi=prices[i]
            else:
                pro=prices[i]-mi
                if(pro>ma):
                    ma=pro
        return ma