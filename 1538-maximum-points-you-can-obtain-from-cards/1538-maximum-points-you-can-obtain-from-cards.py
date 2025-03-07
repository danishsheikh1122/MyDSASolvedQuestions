class Solution(object):
    def maxScore(self, li, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        lsum=sum(li[:k])
        rsum=0
        end_index=len(li)-1

        max_sum=lsum

        for i in range(k-1,-1,-1):
            # print(i,end_index)
            print(lsum,rsum)
            lsum-=li[i]
            rsum+=li[end_index]
            end_index-=1

            max_sum=max(max_sum,lsum+rsum)
        return max_sum