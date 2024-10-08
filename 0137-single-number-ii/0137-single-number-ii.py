class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Brute Force

        di={}
        for i in nums:
            di[i]=di[i]+1 if i in di else 1

        for key,value in di.items():
            if value==1:
                return key
        # TC-On-pass 
        # SC-on
        # ------------------------------------
        # Better solution 
        for i in nums:
            if nums.count(i)==1:
                return i