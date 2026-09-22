class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, best = 0, 0
        seen = set()

        for right, c in enumerate(s):
            while c in seen:
                seen.remove(s[left])
                left += 1
            seen.add(c)
            best = max(best, right - left + 1)
        return best