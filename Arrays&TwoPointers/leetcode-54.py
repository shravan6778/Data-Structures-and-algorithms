'''Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100'''

from typing import List
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    n=len(matrix)
    m=len(matrix[0])
    total=m*n
    count=0
    newarr=[]
    rowstart,rowend,colstart,colend=0,n-1,0,m-1
    while count<total:
        for i in range(colend,colend+1):
            newarr.append(matrix[rowstart][i])
            count+=1
        rowstart+=1
        if count==total:
            break
        for i in range(rowstart,rowend+1):
            newarr.append(matrix[i][colend])
            count+=1
        colend-=1
        if count==total:
            break
        for i in range(colend,colstart-1,-1):
            newarr.append(matrix[rowend][i])
            count+=1
        rowend-=1
        if count==total:
            break
        for i in range(rowend,rowstart-1,-1):
            newarr.append(matrix[i][colstart])
            count+=1
        colstart+=1
    return newarr
    