class Solution(object):
    def findMaxConsecutiveOnes(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_count=result=0

        for i in n:
            if i==1:
                result+=1
                max_count=max(max_count,result)
            else:
                result=0
        return max_count
        