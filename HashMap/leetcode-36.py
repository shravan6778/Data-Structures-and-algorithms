'''Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.'''

from typing import List
def isValidSudoku(self, board: List[List[str]]) -> bool:
        hr={}
        #row-wise
        for i in board:
            for j in i:
                if j in hr and j!='.':
                    return False
                else:
                    hr[j]=True
            print(hr)
            hr={}
        #column-wise
        hc={}
        for i in range(len(board)):
            for j in board:
                if j[i] in hc and j[i]!='.':
                    return False
                else:
                    hc[j[i]]=True
            print(hc)
            hc={}
        #for 3*3 
        hj={}
        hk={}
        hl={}
        for i in range(len(board)):
            
            for j in range(3):
                if board[i][j] in hj and board[i][j]!='.':
                    return False
                else:
                    hj[board[i][j]]=True
            for k in range(3,6):
                if board[i][k] in hk and board[i][k]!='.':
                    return False
                else:
                    hk[board[i][k]]=True
            for l in range(6,9):
                if board[i][l] in hl and board[i][l]!='.':
                    return False
                else:
                    hl[board[i][l]]=True
            if (i+1)%3==0:
                hj={}
                hk={}
                hl={}
        return True