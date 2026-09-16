class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        box = defaultdict(list)

        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                if cur == '.':
                    continue
                elif cur in rows[r] or cur in cols[c] or cur in box[(r // 3, c // 3)]:
                    return False
                else:
                    rows[r].append(cur)
                    cols[c].append(cur)
                    box[(r // 3, c // 3)].append(cur)
        
        return True