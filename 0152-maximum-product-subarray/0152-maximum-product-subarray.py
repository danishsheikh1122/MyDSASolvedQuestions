class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums)==1:
        #     return nums[0]
        # product=0
        # for i in range(len(nums)):
        #     pro=nums[i]
        #     for j in range(i+1,len(nums)):
        #         pro*=nums[j]
        #         product=max(product,pro)
        # return product

        max_so_far = nums[0]
        min_so_far = nums[0]
        max_product = nums[0]

        for i in range(1, len(nums)):
            temp_max = max(nums[i], max_so_far * nums[i], min_so_far * nums[i])
            min_so_far = min(nums[i], max_so_far * nums[i], min_so_far * nums[i])
            max_so_far = temp_max
            max_product = max(max_product, max_so_far)

        return max_product