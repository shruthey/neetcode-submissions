class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        best = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                best = max(best, prices[right] - prices[left])
            right += 1
        return best