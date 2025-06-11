class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        di=Counter(nums)
        resArr=[]
        count=0
        # if len(nums)<3:return list(set(nums))

        for k,v in di.items():
            if v>(len(nums)//3):
                resArr.append(k)
            else:
                count+=1
        return resArr

        # resArr=[]
        # for i in range(len(nums)):
        #     count=0
        #     for j in range(len(nums)):
        #         if i!=j:
        #             if nums[i]==nums[j]:
        #                 count+=1
        #         if count>(len(nums)/3):
        #             resArr.append(nums[i])
        # return resArr


            
        