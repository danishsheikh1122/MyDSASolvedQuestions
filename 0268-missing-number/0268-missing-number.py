class Solution(object):
    def missingNumber(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force worst solution posible
        # min_n=0
        # max_n=len(n)
        # li=[x for x in range(min_n,max_n+1)]
        # # print(li)
        # for i in li:
        #     if(i not in n):
        #         print(i)
        #         return i
        # return 0

        minn=0
        maxx=max(n)+1

        for i in range(maxx+1):
            if(i not in n):
                return i
        return 0
