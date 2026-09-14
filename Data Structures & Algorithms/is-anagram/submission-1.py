class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        sCount = {}
        tCount = {}
        for p, q in zip(s, t):
            sCount[p] = sCount.get(p, 0) + 1
            tCount[q] = tCount.get(q, 0) + 1

        return sCount == tCount