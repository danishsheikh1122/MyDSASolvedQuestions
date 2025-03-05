class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxx=l=r=zeros=0
        while r<len(nums):
            if nums[r]==0:
                zeros+=1
                while zeros>k:
                    if nums[l]==0:
                        zeros-=1
                    l+=1
            maxx=max(maxx,r-l+1)
            r+=1
        return maxx
