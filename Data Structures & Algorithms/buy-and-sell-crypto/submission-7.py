class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                best = max(best, prices[right] - prices[left])
            right += 1
        return best