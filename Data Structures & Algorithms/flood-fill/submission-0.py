class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old = image[sr][sc]
        new = color
        R, C = len(image), len(image[0])
        if old == new:
            return image

        def dfs(r, c):
            if image[r][c] != new and image[r][c] == old:
                image[r][c] = new
                if r+1 < R:
                    dfs(r+1, c)
                if r-1 >= 0:
                    dfs(r-1, c)
                if c+1 < C:
                    dfs(r, c+1)
                if c-1 >= 0:
                    dfs(r, c-1)

        dfs(sr, sc)
        return image