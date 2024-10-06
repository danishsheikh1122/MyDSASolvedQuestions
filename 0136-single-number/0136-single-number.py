class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        using bit wise operator ^ xor
        5^5=5 but if 5^6 op will be diff so we can easily use it to 
        identify diff element from an array
        """
        res_xor=0 
        for i in nums:
            res_xor^=i
        return res_xor



        