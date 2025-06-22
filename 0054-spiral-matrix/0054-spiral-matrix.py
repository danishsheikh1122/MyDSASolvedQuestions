class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # res = []
        # top, bottom = 0, len(matrix) - 1
        # left, right = 0, len(matrix[0]) - 1
        # res_arr=[]
    
        # while top<=bottom and left<=right:
        #     # for top row
        #     for i in range(left,right+1):
        #         res_arr.append(matrix[top][i])
        #     top+=1
        #     # for right column 
        #     for i in range(top,bottom+1):
        #         res_arr.append(matrix[i][right])
        #     right-=1

        #     if top<=bottom:
        #         for i in range(right,left-1,-1):
        #             res_arr.append(matrix[bottom][i])
        #         bottom-=1
        #     if left<=right:
        #         for i in range(bottom,top-1,-1):
        #             res_arr.append(matrix[i][left])
        #         left+=1
        # return res_arr
        res=[]
        left=0
        top=0
        right=len(matrix[0])-1#rows
        bottom=len(matrix)-1#cols
        while top<=bottom and left<=right:
            # top row
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1

            # right col
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1

            # bottom row
            if(top<=bottom):
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom-=1
            
            # left col
            if (left<=right):
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
            left+=1

        return res

        



























