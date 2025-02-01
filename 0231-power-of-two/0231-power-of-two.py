class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # just minus n-1 and and it with n
        # if 2->0010 and 2-1=0001
        # now perform logical anding 
        # 0010&0001 ->1&1=1 else answer will be 0
        if n==0:
            return False
        # n==0 is the edge case
        res=True if  (n & (n-1) ) ==0  else False
        return res


