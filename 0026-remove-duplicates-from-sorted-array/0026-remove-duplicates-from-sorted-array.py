class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force approach using extra space
        new_arr=[]
        for num in nums:
            if num not in new_arr:
                new_arr.append(num)
        for i in range(len(new_arr)):
            nums[i]=new_arr[i]
            
        return len(new_arr)
        
        
        # # optimal using two pointers  
        # l=1 
        # r=l+1
        # while r<=len(nums):
        #     if nums[r]!=nums[l]:
        #         nums[l]=nums[r]
        #         l+=1
        #     r+=1
        # return l
        