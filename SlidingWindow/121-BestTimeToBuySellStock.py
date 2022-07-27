class Solution:
    def maxProfit(self, prices) -> int:
        # can't sell before buying so
        left, right, profit = 0, 1, 0

        while right < len(prices):
            if prices[left] < prices[right]:
                tmpProfit = prices[right] - prices[left]
                if tmpProfit > profit:
                    profit = tmpProfit
            else:
                left = right
            right += 1
        return profit
