class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        res = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                res = max(res, prices[right] - prices[left])

            right += 1

        return res
        