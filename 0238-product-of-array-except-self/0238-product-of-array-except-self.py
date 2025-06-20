class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # login in free foam
        # l=[1]
        # r=[1] *len(nums)
        # j=0
        # for i in range(len(nums)-1):
        #     l.append(l[i]*nums[i])
        #     j+=1
        # j=len(nums)-2
        # for i in range(len(nums)-1,-1,-1):
        #     r[j]=r[j+1]*nums[i]
        #     j-=1
        # r[len(nums)-1]=1
        # print(r)

        # for i in range(len(nums)):
        #     l[i]=l[i]*r[i]
        # return l
        # new approach from soultions
        # res_arr=[1]*len(nums)
        # l=1
        # for i in range(len(nums)):
        #     res_arr[i]*=l
        #     l*=nums[i]
        # r=1
        # for i in range(len(nums)-1,-1,-1):
        #     res_arr[i]*=r
        #     r*=nums[i]
        # return res_arr

        # res_arr=[1]*len(nums)
        # l=r=1
        # for i in range(len(nums)):
        #     res_arr[i]*=l
        #     l*=nums[i]
        
        # for i in range(len(nums)-1,-1,-1):
        #     res_arr[i]*=r
        #     r*=nums[i]
        # return res_arr

        # new_arr=[]
        # for i in range(len(nums)):
        #     prod=1
        #     for j in range(len(nums)):
        #         if i!=j:
        #             prod*=nums[j]
        #     new_arr.append(prod)
        # return new_arr

        res=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]*=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res


        
        






























    