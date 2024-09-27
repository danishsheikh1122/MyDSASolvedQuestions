class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # just joikng , dont use inbuilt functions
        # nums.sort()
        

        # approach just count no of 0 1 2 and in that array put it 
        # li=[]
        # no_z=0
        # no_o=0
        # no_t=0
        # for i in nums:
        #     if(i==0):
        #         no_z+=1
        #     elif(i==1):
        #         no_o+=1
        #     elif(i==2):
        #         no_t+=1
        #     else:
        #         continue
        # # print(no_z,no_o,no_t)

        # while no_z>0 or no_o>0 or no_t>0:
        #     if(no_z!=0):
        #         li.append(0)
        #         no_z-=1
        #     elif(no_o!=0):
        #         li.append(1)
        #         no_o-=1
        #     elif(no_t!=0):
        #         no_t-=1
        #         li.append(2)
        #     else:
        #         continue
        # # nums=li
        # # print(li)
        # for i in range(0,len(li)):
        #     nums[i]=li[i]
        #     # print(i)
        # # print(nums)

        #another approach

         # approach just count no of 0 1 2 and in that array put it 
        # li=[]
        # no_z=0
        # no_o=0
        # no_t=0
        # for i in nums:
        #     if(i==0):
        #         no_z+=1
        #     elif(i==1):
        #         no_o+=1
        #     elif(i==2):
        #         no_t+=1
        #     else:
        #         continue
        # # print(no_z,no_o,no_t)
        # i=0
        # while no_z>0 or no_o>0 or no_t>0:
        #     if(no_z!=0):

        #         nums[i]=0
        #         no_z-=1
        #         i+=1
        #     elif(no_o!=0):
        #         nums[i]=1
        #         no_o-=1
        #         i+=1
        #     elif(no_t!=0):
        #         nums[i]=2
        #         no_t-=1
        #         i+=1
        #     else:
        #         continue
        # nums=li
        # print(li)
        # for i in range(0,len(li)):
        #     nums[i]=li[i]
            # print(i)
        # print(nums)



        '''
        using 2 pointers approach to solve this problem 
        l=0 r=len(nums)-1
        loop while l<r
        l>r and l-r>0:
        swap using xor operator
        l+=1

        l<r
        l+=1
        swap

        else
        if()
        r-=1

        l0
        r5
        0 0 2 1 1 2

        l1 
        r4
        0 0 2 1 1 2

        l1 
        r3
        



        '''

        l=0
        c=0
        r=len(nums)-1

        while c<r:
            if nums[c]==0:
                nums[c],nums[l]=nums[l],nums[c]
                l+=1
                c+=1
            elif nums[c]==1:
                c+=1
            else:#if nums[l]==2
                nums[c],nums[r]=nums[r],nums[c]
                r-=1
            





           