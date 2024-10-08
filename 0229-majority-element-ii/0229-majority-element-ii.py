class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # USING HASH MAPS AND SC-ON
        # di=defaultdict(int)
        # for i in nums:
        #     di[i]+=1
        # li=[]
        # for key,value in di.items():
        #     if value>len(nums)//3:
        #         li.append(key)
        # return li

        # ------------------------------
        # we have to find all the mj elements from an arr using moores algorithm
        # but we know that there will be at most 2 mj elements
        # so taking 2 mj_elem and 2 counter 

        mj1=0
        mj2=0
        c1=c2=0

        for i in range(len(nums)):
            if c1==0 and nums[i]!=mj2:
                c1=1
                mj1=nums[i]
            elif c2==0 and nums[i]!=mj1:
                c2=1
                mj2=nums[i]
            
            elif mj1==nums[i]:
                c1+=1
            elif mj2==nums[i]:
                c2+=1
            else:
                c1-=1
                c2-=1

        print(mj1,mj2)

        c1=c2=0


        for i in nums:
                if mj1==i:
                    c1+=1
                elif mj2==i:
                    c2+=1
        li=[]
        if c1>(len(nums)//3):
            li.append(mj1)
            
        if c2>(len(nums)//3):
            li.append(mj2)
        # print(li)
        return li




