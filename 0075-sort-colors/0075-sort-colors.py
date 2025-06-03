class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Fuckkkkkkk lol
        # nums.sort()

        # counting sort algorithm
        # first count all the numbers r w b and then put it in the nums arr

        num_r=num_w=num_b=0
        for num in nums:
            if num==0:
                num_r+=1
            elif num==1:
                num_w+=1
            else:
                num_b+=1
        
        nums[:num_r]=[0]*num_r
        nums[num_r:num_r+num_w]=[1]*num_w
        nums[num_r+num_w:]=[2]*num_b
        print(nums)

