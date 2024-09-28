class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n=bin(n)

        # from collections import Counter
        # ct=Counter(n)
        # print(ct['1'])
        # return ct['1']

        # above is brute force and worst appoach 
        # n-=1
        # print(n & n)
        
        # basic idea is to make n 0 and while making it zero inc ans

        res=0
        while n!=0:
            res+=1
            n=n & n-1
        return res 