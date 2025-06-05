class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max_sum=nums[0]
        # for i in range(len(nums)):
        #     res=0
        #     for j in range(i+1,len(nums)):
        #         res+=nums[j]
        #         max_sum=max(max_sum,res)

        # return max_sum
        if len(nums)==1:
            return nums[0]
        max_sum=nums[0]
        sum=0

        for num in nums:
            if sum<0:
                sum=0
            sum+=num
            max_sum=max(max_sum,sum)
        return max_sum