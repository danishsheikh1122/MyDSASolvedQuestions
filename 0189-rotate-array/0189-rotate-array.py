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
        # k=k%len(nums)
        # rotated=[0]*len(nums)
        # for i in range(len(nums)):
        #     rotated[(i+k)%len(nums)]=nums[i]


        # for i in range(len(nums)):
        #     nums[i] = rotated[i] 

        # rotate the full array
        def reverse(nums,start,end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
            return nums
        k=k%len(nums)
        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)
