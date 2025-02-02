class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """ 
        temp_res=start^goal
        res=bin(temp_res)[2:]

        return sum(1 for bit in res if bit == '1')