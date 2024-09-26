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
        # another approach
        # nums.sort()
        # start=nums[0]

        # for i in range(1,len(nums)):
        #     if(nums[i]==nums[i-1]):
        #         return True
        # return False
        # --------------------------------
        # another approach with 
        # a=len(nums)
        # nums=set(nums)
        # print(nums)
        # if(len(nums)<a):
        #     return True
        # else:
        #     return False
        # --------------------------------
        # another approach with hash maps
        # di={}
        # for i in nums:
        #     di[i]=di[i]+1 if i in di else 1
        # for key,values in di.items():
        #     if(values>1):
        #         return True
        # return False

        # best above 
        # TC=O(n)
        # Sc=O(n)

        h=set()
        for num in nums:
            if num in h:
                return True
            else:
                h.add(num)
        return False