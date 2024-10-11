class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # make this prob as find the max_len of with at most k zeros
        

        # sliding window
        # l=r=max_len=no_zeros=0

        # while r<len(nums):
        #     if nums[r]==0:
        #         no_zeros+=1
        #     while no_zeros>k:
        #         if nums[l]==0:
        #             no_zeros-=1
        #         l+=1
        #     if no_zeros<=k:
        #         max_len=max(max_len,r-l+1)
        #     r+=1
        # return max_len
        # tc-2on still we can make it more optimal
        # --------------------------------------

        l=r=max_len=zero=0

        while r<len(nums):
            if nums[r]==0:
                zero+=1
            if zero>k:
                if nums[l]==0:
                    zero-=1
                l+=1
            if zero<=k:
                max_len=max(max_len,r-l+1)
            r+=1
        return max_len

        # tc- 1N and sc o1