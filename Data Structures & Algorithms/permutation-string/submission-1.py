class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        left = 0

        for right, c in enumerate(s2, start=len(s1)-1):
            if Counter(s1) == Counter(s2[left:right+1]):
                return True
            else:
                left += 1
        return False