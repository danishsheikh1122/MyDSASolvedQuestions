class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # TLE
        # # for i in nums:
        # #     if(nums.count(i)>=2):
        # #         return True
        # # return False
        # ------------------------------------------ 
        # nums.sort()
        # start=nums[0]

        # for i in range(1,len(nums)):
        #     if(nums[i]==nums[i-1]):
        #         return True
        # return False
        # another approach with 
        a=len(nums)
        nums=set(nums)
        print(nums)
        if(len(nums)<a):
            return True
        else:
            return False