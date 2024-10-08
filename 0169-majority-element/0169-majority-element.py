import math 
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        use a hash table store the count and
        while final looping if num appear more tha num/2 then print it
        """
        # maxx=max(n)
        # li=[0]*(maxx+1)
        # # print(li)    

        # for i in n:
        #     li[i]+=1
        # print(li)    
        # # now return max from hash map
        
        # res=max(li)
        # return li.index(res)

        # this code gives memory limit exceed so another method

# ----------------------------------------------------------------------    
        # using hash table ds as a DICTIONARY
        # tc-sc-on
        # from collections import defaultdict

        # di={}
        # # print(di[0])

        # for i in n:
        #     di[i]=di[i]+1 if i in di else 1
        # # print(di)

        # for key,value in di.items():
        #     if value>len(n)//2:
        #         return key
        # return 0

        # ------------------------------------------
        # USE MOORES VOTING ALGO TO SOLVE THIS


        # MOORES ALGO TO FIND MAJORITY ELEM FROM AN ARR

        # TC ON -SC O(1)

        mj_elem=0

        count=0

        for i in range(len(nums)):
            if count==0:
                count+=1
                mj_elem=nums[i]
            elif nums[i]==mj_elem:
                count+=1
            else:
                count-=1
        count=0
        for i in nums:
            if i ==mj_elem:
                count+=1 
        if count>len(nums)/2:
            return mj_elem
        else:
            return nums



