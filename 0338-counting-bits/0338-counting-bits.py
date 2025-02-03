class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        li = []
        for i in range(n+1):
            res = 0
            x = i
            while x:
                res += x & 1  
                x >>= 1       
            li.append(res)
        return li