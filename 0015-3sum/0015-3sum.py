class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # # i is normal ptr and j,k is l anr r resp
        # n.sort()
        # res=set()
        # for i in range(0,len(n)):
        #     l=i+1
        #     r=len(n)-1
        #     # this if makes code faster if i ==i-1 then same number so move to non similar number 
        #     if i>0 and n[i]==n[i-1]:
        #         continue
        #     while l<r:
        #         isZero=n[i]+n[l]+n[r]

        #         if isZero==0:
        #             res.add((n[i],n[l],n[r]))
        #             l+=1
        #             r-=1

        #             # this 2 while loops makes the code fast 
        #             # if same elem appear then it will jumn to next non similar  number
        #             while l<r and n[l]==n[l-1]:
        #                 l+=1
        #             while l<r and n[r]==n[r+1]:
        #                 r-=1
        #         elif isZero<0:
        #             l+=1
        #         else:
        #             r-=1
        # return list(res)
        # -------------------------------------
        # brute
        # res=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 temp=[nums[i],nums[j],nums[k]]
        # SORTING TRICKY 
        #                 temp.sort()
        #                 res.append(tuple(temp))
        # res=list(set(res))
        # res=[list(t) for t in res]
        # return res

        # optimal 

        nums.sort()
        resArr=[]


        for i in range(len(nums)):
            # [-1 , -1]is same skip  
            if i>0 and nums[i]==nums[i-1]:
                continue

            l=i+1
            r=len(nums)-1
            while l<r:
                summ=nums[i]+nums[l]+nums[r]
                if summ>0:
                    r-=1
                elif summ<0:
                    l+=1
                # final condtn summ==0
                else:
                    resArr.append([nums[i],nums[l],nums[r]])
                    # we are incrementing L as 
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return resArr

         