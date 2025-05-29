class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        len_arr=len(matrix)

        for i in range(0,len_arr):
            for j in range(i+1,len_arr):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix:
            row.reverse()
        
