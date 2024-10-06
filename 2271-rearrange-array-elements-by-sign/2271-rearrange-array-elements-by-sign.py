class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # brute force approach is to make 2 seperate li of +ve and -ve and run a loop to 
        # make final res

        pos=[x for x in nums if x>=0]
        neg=[x for x in nums if x<0]
        res_li=[]
        i=0
        while i!=len(pos):
            res_li.append(pos[i])
            res_li.append(neg[i])
            i+=1
        # print(res_li)
        return res_li
