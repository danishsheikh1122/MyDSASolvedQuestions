class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # closest_num=nums[0]
        # for n in nums:
        #     if abs(n)<abs(closest_num):
        #         closest_num=n
        # if closest_num < 0 and abs(closest_num) in nums:
        #     return abs(closest_num)
        # return closest_num

        # max_number=float('-inf')
        # for i in nums:
        #     if abs(i)<abs(max_number):
        #         max_number=i
        # if max_number<0 and abs(max_number) in nums:
        #         return abs(max_number)
        # else:
        #         return max_number 

        minVal=float("inf")
        for i in nums:
            if abs(i)<abs(minVal):
                minVal=i
        if abs(minVal) in nums:
            return abs(minVal) 
        return minVal




