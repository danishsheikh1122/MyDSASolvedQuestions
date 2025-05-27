class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # intervals.sort(key=lambda interval:interval[0])
        # new_li=[]
        # for interval in intervals:
        #     if not new_li or new_li[-1][1] < interval[0]:
        #         new_li.append(interval)
        #     else:
        #         new_li[-1]=[new_li[-1][0],max(new_li[-1][1],interval[1])]
        # return new_li

        #  onlogn on 

        intervals.sort(key=lambda x:x[0])
        prev=intervals[0]
        res=[]

        for curr_int in intervals:
            if curr_int[0]<=prev[1]:
                prev[1]=max(curr_int[1],prev[1])
            else:
                res.append(prev)
                prev=curr_int
        
        res.append(prev)
        return res