class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # -------------------------------
        # slow solution

        #   l=0
        # n=len(nums)-1
        # r=n

        # while l!=n:
        #     if nums[l]+nums[r]==target:
        #         return [l,r]
        #     elif l+1==r:
        #         l+=1
        #         r=n
        #     else:
        #         r-=1
        # ---------------------------------
        di={}
        for i in range(len(nums)):
            di[nums[i]]=i
        for i in range(len(nums)):
            x=target-nums[i]
            if x in di and di[x]!=i:
                return [i,di[x]]
