class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # brute force
        # di=Counter(nums)
        # di=sorted(di.items(),key=lambda item:-item[0])
        # print(di)
        # res=0
        # i=0
        # for k,v in di:
        #     if i<k:
        #         i+=v
        #         res+=k
        # return res

        # temp=[x for x in nums]
        # temp.sort()
        # summ=temp[-k:]
        # li=[]

        # for i in range(len(nums)):
        #     if nums[i] in summ:
        #         li.append(nums[i])
        #         nums.remove(nums[i])
        # return li

        temp = sorted(nums)[-k:]  
        count = Counter(temp) 
        li = []
        for num in nums:
            if count[num] > 0:
                li.append(num)
                count[num] -= 1
        return li            



        



