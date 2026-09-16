class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while s[left].isalnum() != True and left < right:
                left += 1
            while s[right].isalnum() != True and right > left:
                right -= 1

            if s[left].capitalize() != s[right].capitalize():
                print(s[left].capitalize() , s[right].capitalize())
                return False
            left += 1
            right -= 1

        return True