class Solution(object):
    def findClosestNumber(self, n):
        """
        :type n: List[int]
        :rtype: int

        """
        min_v=n[0]
        for num in n:
            if abs(num)<abs(min_v):
                min_v=num
            elif abs(num)==abs(min_v):
                min_v=max(min_v,num)
        return min_v

        
        