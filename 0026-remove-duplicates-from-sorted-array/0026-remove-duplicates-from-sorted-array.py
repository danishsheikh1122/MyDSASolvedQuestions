class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # index=1
        # for i in range(1,len(nums)):
        #     if(nums[i]!=nums[i-1]):
        #         nums[index]=nums[i]
        #         index+=1
        # return index      



        # using 2 pointers approach


        # i,j i will move from starting and j will act as an index of last uncommon and 
        # i will be as incrementation

        j=1

        for i in range(1,len(nums)):
            if(nums[i]!=nums[i-1]):
                nums[j]=nums[i]
                j+=1

        print(nums)
        return j
