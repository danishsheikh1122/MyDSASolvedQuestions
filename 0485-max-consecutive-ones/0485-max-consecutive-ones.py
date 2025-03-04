class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m_count=count=0
        for i in nums:
            if i ==0:
                count=0
            else:
                count+=1
                m_count=max(m_count,count)
        return m_count

        