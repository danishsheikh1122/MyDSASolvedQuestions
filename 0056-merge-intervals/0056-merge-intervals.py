class Solution(object):
    def merge(self, nums):
        """
        :type i: List[List[int]]
        :rtype: List[List[int]]
        """
        # if len(i)==1:
        #     return i

        # temp=i[0]
        # to_push=[]
        # # print(temp)
        # for n in range(1,len(i)):
        #     # print(i[n][0])
        #     if(temp[0] <= i[n][0] and (temp[1]<=i[n][1] and temp[1]>=i[n][0])):
        #         # print(temp,n)
        #         temp=[temp[0],i[n][1]]
        #         to_push.append(temp)
        #         # print(temp,n)
        #     #     temp=n
        #     else:

        #         if(temp not in to_push):
        #             to_push.append(temp)
        #         to_push.append(i[n])
        # # print(to_push)

        # return to_push


        
        #worng algorithm 





        li=[]
        
        nums.sort()

        for i in range(len(nums)):
            if not li or nums[i][0]>li[-1][1]:
                li.append(nums[i])
            else:
                li[-1][1]=max(li[-1][1],nums[i][1])
        return li














