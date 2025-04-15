class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #List comprehension
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                sqr = board[row][col]
                box = (row // 3) * 3 + (col // 3)
                if sqr == '.':
                    continue
                
                if sqr in rows[row] or sqr in cols[col] or sqr in boxes[box]:
                    return False
                
                rows[row].add(sqr)
                cols[col].add(sqr)
                boxes[box].add(sqr)

        return True
