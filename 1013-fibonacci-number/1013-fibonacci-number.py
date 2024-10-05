class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        # usnig memo->top-down dp

        # memo={0:0,1:1}

        # def recursion(n):
        #     if n in memo:
        #         return memo[n]
        #     else:
        #         memo[n]=recursion(n-2)+recursion(n-1)
        #         return memo[n]
            
        # return recursion(n)

        # on
        # on

        # -----------------------------------------------------

        # bottom up -dp easy peasy :))
        if n==0:
            return 0

        if n==1:
            return 1

        arr=[0]*(n+1)
        arr[0]=0
        arr[1]=1

        for i in range(2,n+1):
            arr[i]=arr[i-2]+arr[i-1]
        return arr[n]




        