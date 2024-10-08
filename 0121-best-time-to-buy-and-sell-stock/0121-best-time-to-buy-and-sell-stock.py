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

        # just keep 2 vars max_p and min_index_value
        # if len(p) ==0:
        #     return 0
        # max_p=0
        # min_index_value=p[0]

        # for i in p:
        #     if i<min_index_value:
        #         min_index_value=i
        #     max_p=max(abs(min_index_value-i),max_p)
        # # print(max_p) 
        # return max_p   
        # if len(p) ==0:
            # return 0
        #-------------------------------------------------- 
        # this is DP -approach
        max_p=0
        cur_min_val=p[0]

        for i in p :
            curr_p=i-cur_min_val
            max_p=max(max_p,curr_p)
            cur_min_val=min(cur_min_val,i)
        return max_p
