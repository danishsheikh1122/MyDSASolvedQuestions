class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """ 
        row=[0]*len(matrix)
        col=[0]*len(matrix[0])

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==0:
                    row[r]=1
                    col[c]=1
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if row[r]==1 or col[c]==1:
                    matrix[r][c]=0
