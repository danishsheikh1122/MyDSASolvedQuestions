class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # just brute force worst solution
        li=[]
        while num:
            if (num&1):
                li.append(0)
            else:
                li.append(1)
            num>>=1
        print(li)
        li=li[::-1]
        strr=''
        for char in li:
            strr+=str(char)
        return int(strr,2)

