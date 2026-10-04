# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        Q = deque([root])
        level = 0

        while Q:
            for i in range(len(Q)):
                node = Q.popleft()

                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            level += 1
        return level

            