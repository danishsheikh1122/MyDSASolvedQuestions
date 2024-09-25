class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        di=defaultdict(int)
        for i in nums:
            di[i]+=1
        li=[]
        for key,value in di.items():
            if value>len(nums)//3:
                li.append(key)
        return li
            
        