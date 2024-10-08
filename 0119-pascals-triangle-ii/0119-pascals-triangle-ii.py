class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        li=[]
        li.append([1])

        for i in range(1,rowIndex+1):
            prev_elems=li[i-1]
            curr_li=[1]

            for j in range(1,i):
                curr_li.append(prev_elems[j-1]+prev_elems[j])
            curr_li.append(1)
            li.append(curr_li)
        return li[rowIndex]
        