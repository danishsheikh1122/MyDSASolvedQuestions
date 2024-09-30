class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # dup=None
        # without_dups=set()


        # index=0
        # for n in nums:
        #     if n in without_dups:
        #         dup=n
        #         if n!=1:
        #             index=nums.index(n)
        #     else:
        #         without_dups.add(n)
        # print(index)

                            

        
        # from collections import Counter

        di=Counter(nums)
        dup=missing=None
        for key,value in di.items():
            if value>1:
                dup=key
        index=1
        for key in range(1,len(nums)+1):
            if(di[key]==0):
                missing=key
                return [dup,missing]
            index+=1

                # print(key,value)
                # if di[key-1]==0 and key-1!=0:
                #     return [key,key-1]
                # else:
                #     return [key,k]
                


          
        # for i in range(1, len(nums) + 1):
        #     count = nums.count(i)
        #     if count == 2:
        #         dup = i
        #     elif count == 0:
        #         missing = i
        
        # return [dup, missing]
    