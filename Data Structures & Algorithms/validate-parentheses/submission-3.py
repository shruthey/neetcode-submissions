class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c not in pairs:
                stack.append(c)
            elif not stack or pairs[c] != stack[-1]:
                return False
            else:
                stack.pop()

        return len(stack) == 0