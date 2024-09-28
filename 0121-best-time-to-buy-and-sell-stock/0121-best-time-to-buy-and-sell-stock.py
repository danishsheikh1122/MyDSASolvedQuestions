class Solution(object):
    def maxProfit(self, p):
        """
        :type prices: List[int]
        :rtype: int
        """
        # brute force approach
        # TLE
        # max_p=0
        # for i in range(0,len(p)):
        #     for j in range(i+1,len(p)):
        #         print(max_p,i,j)
        #         if p[i]<p[j] and max_p<abs((p[i]-p[j])):
        #             max_p=abs((p[i]-p[j]))
        #             print(max_p)
        # return max_p
        # -----------------------------------------------------

        # just keep 2 vars max_p and min_index

        max_p=0
        min_index=float('inf')#infinity

        for i in p:
            if i<min_index:
                min_index=i
            max_p=max(abs(min_index-i),max_p)
        # print(max_p) 
        return max_p   

