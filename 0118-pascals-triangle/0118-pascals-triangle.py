class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        li=[]
        
        if numRows==0:
            return li
        f_row=[1]
        li.append(f_row)
        
        for i in range(1,numRows):
            prev_row=li[i-1]
            curr_row=[1]

            for j in range(1,i):
                # print(prev_row[j-1],prev_row[j])
                res=prev_row[j-1]+prev_row[j]
                curr_row.append(res)

            curr_row.append(1)
            li.append(curr_row)

        return li


