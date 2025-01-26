class Solution(object):
    def intersect(self, n1, n2):
        """
        :type n1: List[int]
        :type n2: List[int]
        :rtype: List[int]

        # the brute force approach will be is to first 9
        """
        # -------------------------------
        # this is good approach 
        # if (len(n1) or len(n2))== 0:
        #     return []
        # n1.sort()
        # n2.sort()
        # li=[]
        # for i in n1:
        #     if i in n2:
        #         # print(i)
        #         li.append(i)
        #         n2.remove(i)
        # return li
        # tc o n*m  and sc on
        # coz we are using (in) inside loop 

        # ---------------------------------
        # now by using hash table more optimal solution 

        di=Counter(n1)
        for i in range(len(n1)):
            n1.pop()

        for n in n2:
            if(n in di and di[n]>0):
                n1.append(n)
                di[n]-=1
        return n1

