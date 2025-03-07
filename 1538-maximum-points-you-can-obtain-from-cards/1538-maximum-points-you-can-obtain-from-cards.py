class Solution(object):
    def maxScore(self, li, k):
        """
        :type li: List[int]
        :type k: int
        :rtype: int
        """
        left_sum=sum(li[:k])
        right_sum=0
        end_index=len(li)-1
        max_sum=left_sum

        for i in range(k-1,-1,-1):
                           #will run till 0 and -1 in every iteration
            left_sum-=li[i] 
            right_sum+=li[end_index]
            max_sum=max(max_sum,left_sum+right_sum)
            end_index-=1
        return max_sum