class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Extreme Brute Force
        # res_li=[]
        # di=Counter(nums)
        # if(di):
        #     res_li.append(max(di))
        #     di.pop(max(di))

        # if(di):
        #     res_li.append(max(di))
        #     di.pop(max(di))
        # if(di):
        #     res_li.append(max(di))

        # if len(res_li)!=3:
        #     return max(res_li)
        # return res_li[-1]

        # Tc-on
        # sc-on

        # ---------------------------------------------

        # first sort the nums and then count if len>=3 then print -3 else max of li
        nums=list(set(nums))
        nums.sort()
        if len(nums)>=3:
            print(nums[-3])
            return nums[-3]

        return max(nums)