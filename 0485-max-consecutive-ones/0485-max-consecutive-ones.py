class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # full working logic with conditional statements
        # m_count=count=0
        # for i in nums:
        #     if i ==0:
        #         count=0
        #     else:
        #         count+=1
        #         m_count=max(m_count,count)
        # return m_count

        # full working without conditional statements
        # max_count = 0
        # current_count = 0
        # for num in nums:
        #     current_count = current_count * num + num # here is the logic 
        #     max_count = max(max_count, current_count)
        # return max_count
        count=0
        max_count=0
        for i in range(len(nums)):
            if nums[i]!=0:
                count+=1
                max_count=max(max_count,count)
            elif nums[i]==0:
                count=0
        return max_count