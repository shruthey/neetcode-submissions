class Solution:
    def isPalindrome(self, s: str) -> bool:
        full = str()
        for c in s:
            if c.isalnum():
                full += c.lower()
        return full == "".join(reversed(full))