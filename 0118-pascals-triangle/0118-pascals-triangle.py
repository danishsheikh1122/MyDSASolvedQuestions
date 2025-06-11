class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        resArr=[[1]]
        for i in range(numRows-1):
            temp=[0]+resArr[-1]+[0]
            row=[]
            for j in range(len(resArr[-1])+1):
                row.append(temp[j]+temp[j+1])
            resArr.append(row)
        return resArr


        