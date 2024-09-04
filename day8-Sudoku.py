"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
https://leetcode.com/problems/valid-sudoku/description/
"""
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to track the digits in rows, columns, and sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                if num == '.':
                    continue  
                
              
                box_index = (i // 3) * 3 + j // 3
                
              
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False
                
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)
      
        return True
solution = Solution()
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(solution.isValidSudoku(board)) 
