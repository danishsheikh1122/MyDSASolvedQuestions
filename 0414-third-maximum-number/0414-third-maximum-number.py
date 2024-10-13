class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res_li=[]
        di=Counter(nums)
        if(di):
            res_li.append(max(di))
            di.pop(max(di))

        if(di):
            res_li.append(max(di))
            di.pop(max(di))
        if(di):
            res_li.append(max(di))

        if len(res_li)!=3:
            return max(res_li)
        return res_li[-1]