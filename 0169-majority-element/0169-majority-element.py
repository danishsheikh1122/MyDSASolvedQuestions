import math 
class Solution(object):
    def majorityElement(self, n):
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

        # from collections import defaultdict

        di=defaultdict(int)
        # print(di[0])

        for i in n:
            di[i]+=1
        # print(di)

        for key,value in di.items():
            if value>len(n)//2:
                return key
        return 0





