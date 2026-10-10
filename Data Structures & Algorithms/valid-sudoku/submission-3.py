class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                tile = board[row][col]
                if tile == ".":
                    continue
                
                box = (row // 3, col //3)

                if (tile in rows[row] or
                    tile in cols[col] or
                    tile in boxes[box]):
                    return False
                
                rows[row].add(tile)
                cols[col].add(tile)
                boxes[box].add(tile)

        return True 


