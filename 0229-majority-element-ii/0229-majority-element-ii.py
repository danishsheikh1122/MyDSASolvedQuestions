class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        di=Counter(nums)
        resArr=[]
        count=0
        if len(nums)<3:return list(set(nums))

        for k,v in di.items():
            if v>(len(nums)/3):
                resArr.append(k)
            else:
                count+=1
        return resArr

            
        