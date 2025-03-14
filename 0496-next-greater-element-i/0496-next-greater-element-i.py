class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # good solution 
        # di={}
        # li=[]
        # for i in range(len(nums2)):
        #     di[nums2[i]]=i
        # print(di)
        # for i in range(len(nums1)):
        #     if nums1[i] in di:
        #         index=di[nums1[i]]+1
        #         found=False
        #         while index<len(nums2):
        #             if nums2[index] > nums1[i]:
        #                 li.append(nums2[index])  
        #                 found = True
        #                 break  
        #             index += 1
                
        #         if not found:
        #             li.append(-1)
        # return li
        #  Time Complexity: O(m + k * n) or O(m^2) in the worst case. - Space Complexity: O(m + k).

        # -------------------------------------------
        # now using monotonic stack to solve this problem 
        # below solution is not for this problem 
        # nge=[]
        # m_stack=[]
        # top=-1

        # for i in range(len(arr),-1,-1):
        #     while top!=-1 and m_stack<=arr[i]:
        #         m_stack.pop()
        #     if top==-1:
        #         nge[i]=-1
        #     else:
        #         nge[i]=m_stack[top]
        #     m_stack.append(arr[i])
        #     top+=1
        # return nge

        di = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack_monotonic = []

        for current_val in nums2:
            while stack_monotonic and current_val > stack_monotonic[-1]:
                value = stack_monotonic.pop()
                if value in di:  # Ensure value exists in nums1
                    value_index = di[value]
                    res[value_index] = current_val
            if current_val in di:
                stack_monotonic.append(current_val)

        return res
