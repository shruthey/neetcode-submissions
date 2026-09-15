class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter()
        res = []

        for n in nums:
            freq[n] += 1

        for key, val in freq.most_common(k):
            res.append(key)
        
        return res