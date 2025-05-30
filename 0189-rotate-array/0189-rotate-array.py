class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # good solution but te 34/38 very good 
        # k=k%len(nums)

        # for i in range(k):
        #     temp=nums[-1]
        #     for j in range(len(nums)-1,-1,-1):
        #         nums[j]=nums[j-1]
        #     nums[0]=temp
        # return nums

        # optimal solution striver
        k=k%len(nums)
        rotated=[0]*len(nums)
        for i in range(len(nums)):
            rotated[(i+k)%len(nums)]=nums[i]


        for i in range(len(nums)):
            nums[i] = rotated[i]
