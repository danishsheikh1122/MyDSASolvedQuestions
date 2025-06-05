class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos_arr=[x for x in nums if x>=0]
        neg_arr=[x for x in nums if x<0]
        # print(pos_arr,neg_arr)
        count_nums=0
        count_arr=0
        for i in range(len(nums)/2):
            nums[count_nums]=pos_arr[count_arr]
            count_nums+=1
            nums[count_nums]=neg_arr[count_arr]
            count_nums+=1
            count_arr+=1
        return nums
        