class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # l_nums2=0
        # for i in range(len(nums1)):
        #     if(i>=m and nums1[i]==0):
        #         nums1[i]=nums2[l_nums2]
        #         l_nums2+=1
        #         # print(l_nums2)
        # # print(nums1)
        # nums1.sort()
        # bute force approach 
        
        for i in range(n):
            nums1[m+i]=nums2[i]
        nums1.sort()
        return nums1








        