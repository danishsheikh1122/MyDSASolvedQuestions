class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack_mono=[]
        nge=[-1]*len(nums)
        lenn=len(nums)

        for i in range((lenn*2)-1,-1,-1):
            while stack_mono and stack_mono[-1]<=nums[i%lenn]:
                stack_mono.pop()
            if i<lenn:
                nge[i]=stack_mono[-1] if stack_mono else -1
            stack_mono.append(nums[i%lenn])
        return nge