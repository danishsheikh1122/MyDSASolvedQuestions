class Solution(object):
    def moveZeroes(self, n):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        2 ptr approach 
        if(n[l]==0):
            temp=n[l]
            n[l]=n[r]
            n[l]=temp
            l+=1
            r-=1
        else:
            l+=1
        """
        # l=0
        # r=len(n)-1

        # while l<r:
        #     if(n[l]==0):
        #         print("ok")
        #         temp=n[l]
        #         n[l]=n[r]
        #         n[r]=temp
        #         l+=1
        #         r-=1
        #     else:
        #         l+=1
        # print(n)

        arr_len=len(n)-1
        new_li=[x for x in n if x!=0]
        # print(new_li)
        for i in range(len(new_li)-1,arr_len):
            new_li.append(0)
        # print(new_li)

        for i in range(0,len(new_li)):
            n[i]=new_li[i]