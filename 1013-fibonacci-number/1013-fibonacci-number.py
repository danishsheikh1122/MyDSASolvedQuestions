class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        # usnig memo->top-down dp

        memo={0:0,1:1}

        def recursion(n):
            if n in memo:
                return memo[n]
            else:
                memo[n]=recursion(n-2)+recursion(n-1)
                return memo[n]
            
        return recursion(n)
        