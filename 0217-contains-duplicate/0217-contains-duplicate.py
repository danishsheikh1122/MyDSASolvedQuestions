class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # # for i in nums:
        # #     if(nums.count(i)>=2):
        # #         return True
        # # return False
        # table_len=abs(min(nums))+max(nums)
        # print(table_len)
        # hash_t=[0]*(table_len)
        # print(table_len,hash_t)
        nums.sort()
        start=nums[0]

        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]):
                return True
        return False
