class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(nums)-1

        while l<r:
            if(nums[l]+nums[r]==target):
                return [l,r]
            elif((l+1)==r):
                l+=1
                r=len(nums)-1
            else:
                r-=1
        print(nums)