class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force approach using extra space remember to return lenght
        # new_arr=[]
        # for num in nums:
        #     if num not in new_arr:
        #         new_arr.append(num)
        # for i in range(len(new_arr)):
        #     nums[i]=new_arr[i]
            
        # return len(new_arr)
        
        
        # # optimal using two pointers  
        l=0
        for r in range(len(nums)):
            if nums[l]!=nums[r]:
                nums[l+1]=nums[r]
                l+=1
        return l+1
        
        