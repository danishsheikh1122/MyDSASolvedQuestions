class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force mine
        di={}
        for i in nums:
            di[i]=1 if i not in di else di[i]+1
        
        for key,value in di.items():
            if value==1:
                return key


        # res=nums[0]
        # for i in range(1,len(nums)):
        #     res^=nums[i]
        # return res

        