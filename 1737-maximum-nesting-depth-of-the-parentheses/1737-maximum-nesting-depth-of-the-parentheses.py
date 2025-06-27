class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=maxCount=0
        for char in s:
            if char=='(':
                count+=1
                maxCount=max(maxCount,count)
            elif char==')':
                count-=1
        return maxCount
        
        