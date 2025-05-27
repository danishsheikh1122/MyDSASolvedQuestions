class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # login in free foam
        l=[1]
        r=[1] *len(nums)
        j=0
        for i in range(len(nums)-1):
            l.append(l[i]*nums[i])
            j+=1
        j=len(nums)-2
        for i in range(len(nums)-1,-1,-1):
            r[j]=r[j+1]*nums[i]
            j-=1
        r[len(nums)-1]=1
        print(r)

        for i in range(len(nums)):
            l[i]=l[i]*r[i]
        return l

    