class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # ptr=0
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         nums[ptr]=nums[i]
        #         ptr+=1
        # while ptr<len(nums):
        #     nums[ptr]=0
        #     ptr+=1


        # my Brute force on on 
        # i=0
        # arr=[]
        # for j in range(len(nums)):
        #     if nums[j]!=0:
        #         arr.append(nums[j])
        #         i+=1
        # for j in range(len(nums)):
        #     if j<i:
        #         nums[j]=arr[j]
        #     else:
        #         nums[j]=0
        if len(nums)==0:
            return nums
        i=0 
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            

        
            




