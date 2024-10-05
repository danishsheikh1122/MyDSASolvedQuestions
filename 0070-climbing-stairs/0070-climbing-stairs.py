class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # using naive recursion
        # def rec(n):
        #     if n==0:
        #         return 1
        #     if n==1:
        #         return 1
            
        #     return (rec(n-1)+rec(n-2))
        # return rec(n)


        # TLE


        # ---------------------------------------
        # top down -memo -dp

        memo={0:1,1:1}

        def rec(n):
            if n in memo:
                return memo[n]
            else:
                memo[n]=rec(n-1)+rec(n-2)
                return memo[n]
        return rec(n)

