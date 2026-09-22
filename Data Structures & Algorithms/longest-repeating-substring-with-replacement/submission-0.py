class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        seen = Counter()
        best = 0

        for right, c in enumerate(s):
            seen[c] += 1
            while (right - left + 1) - seen.most_common(1)[0][1] > k:
                #move left
                seen[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best