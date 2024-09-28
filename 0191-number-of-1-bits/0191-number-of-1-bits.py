class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=bin(n)

        from collections import Counter
        ct=Counter(n)
        print(ct['1'])
        return ct['1']
        