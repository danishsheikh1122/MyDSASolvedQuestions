class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # BRUTE FORCE -TLE
        # max_sum=float('-inf')
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)+1):
        #         summ=sum(nums[i:j])
        #         max_sum=max(summ,max_sum)
        # return max_sum
        
        # --------------------------------------
        # KADAN'S ALGO
        curr_sum=0
        max_sum=float('-inf')

        for i in nums:
            curr_sum+=i
            max_sum=max(max_sum,curr_sum)
            if curr_sum<0:
                curr_sum=0
        return max_sum

