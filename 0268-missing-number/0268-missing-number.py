class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force by me on2

        # for i in range(0,len(nums)+1):
        #     if i not in nums:
        #         return i
        

        # optimal approach
        # by using sum of natural numbers, use formula to calc sum of n natural numbers 
        summ=(len(nums)*(len(nums)+1))/2

        sum_nums=0
        for num in nums:
            sum_nums+=num
        return summ-sum_nums 

