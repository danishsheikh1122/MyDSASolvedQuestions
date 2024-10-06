class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # BRUTE FORCE approach is to make 2 seperate li of +ve and -ve and run a loop to 
        # make final res

        # pos=[x for x in nums if x>=0]
        # neg=[x for x in nums if x<0]
        # res_li=[]
        # i=0
        # while i!=len(pos):
        #     res_li.append(pos[i])
        #     res_li.append(neg[i])
        #     i+=1
        # # print(res_li)
        # return res_li
        # tc-on sc-on
        # -----------------------------------
        # same approach but kind of in place


        # pos=[x for x in nums if x>=0]
        # neg=[x for x in nums if x<0]
        # for i in range(0,len(nums)/2):
        #     nums[i*2]=pos[i]
        #     nums[i*2+1]=neg[i]
        # return nums
        # tc-on sc-on

        # this takes 2 pass as using 2 loops make it in one pass and sc=on

        # -----------------------------------
        # one pass ,tc and sc=on most optimal
        pos=0
        neg=1
        res_li=[0]*len(nums)
        for i in nums:
            if i >=0:
                res_li[pos]=i
                pos+=2
            else:# i >=0:
                res_li[neg]=i
                neg+=2
        # print(res_li)
        return res_li