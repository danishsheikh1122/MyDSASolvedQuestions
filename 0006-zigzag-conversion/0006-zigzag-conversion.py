class Solution(object):
    def convert(self, s, r):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        just create an empty matrix as size of no of rows
        take a var i from 0 to rows-1 and a direction d=0 ir d+=1 and if i==rows-1 then make d-=1

        """
        if r==1:
            return s

        # to create a matrix 
        m=[[] for _ in range(r) ]
        # this will create empty matrix

        i=0
        d=1

        for c in s:
            m[i].append(c)
            if i==0:
                d=1
            elif i==r-1:
                d=-1
            i+=d
        print(m)

        s=""
        for chars in m:
            s+=''.join(chars)
        print(s)
        return s