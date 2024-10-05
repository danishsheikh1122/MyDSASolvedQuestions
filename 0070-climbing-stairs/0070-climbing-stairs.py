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

        # memo={0:1,1:1}

        # def rec(n):
        #     if n in memo:
        #         return memo[n]
        #     else:
        #         memo[n]=rec(n-1)+rec(n-2)
        #         return memo[n]
        # return rec(n)

        # still tc-on and sc-on
        # not efficient


        # bottom up


        if n ==0 or n==1:
            return 1

        arr=[0]*(n+1)
        arr[0]=1
        arr[1]=1
        for i in range(2,n+1):
            arr[i]=arr[i-2]+arr[i-1]
        return arr[n]