class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        create one dict for n1 and check i nums2 is present or ot 
        """
        # from collections import Counter
        # counter=Counter(nums1)
        # print(counter)
        # li=[]

        # for key,value in counter.items():# new key per itr so no redundancy
        #     if key in nums2:
        #         li.append(key)
        # return li




        # Tc-On and Sc-On and runs in 22 beats 91%
        # but more optimal solution is also there
        #------------------------------
        #  using set()

        # n1=set(nums1)
        # n2=set(nums2)

        # # print(n1&n2)
        # return n1&n2
        # not that optimal as previous one 
        # tc-O(1)
        # sc-O(n)
        # runtime 32 ms beats 55
        # so above wala aacha hai 

        #------------------------------ 
        # another approach

        li=set(nums1)
        res_li=[]
        for i in nums2:
            if i in li and i not in res_li:
                res_li.append(i)
        return res_li
    
