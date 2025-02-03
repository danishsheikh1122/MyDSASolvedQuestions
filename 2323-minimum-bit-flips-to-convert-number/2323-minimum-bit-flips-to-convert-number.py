class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """ 
        temp_res=start^goal
        count=0
        # now run a loop while temp-_res and check if lsb & 1 is 1 the count and + else right shift the temo_res until i becomes 0 the loop will continues too run
        while temp_res:
            if temp_res&1:
                count+=1
            temp_res>>=1
        return count