class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        di={}
        li=[]
        for i in range(len(nums2)):
            di[nums2[i]]=i
        print(di)
        for i in range(len(nums1)):
            if nums1[i] in di:
                index=di[nums1[i]]+1
                found=False
                while index<len(nums2):
                    if nums2[index] > nums1[i]:
                        li.append(nums2[index])  
                        found = True
                        break  
                    index += 1
                
                if not found:
                    li.append(-1)
        return li
