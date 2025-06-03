class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        di=Counter(nums)
        max_number=0
        res=0
        print(di)
        
        for key,value in di.items():
            if value>max_number and value>=(len(nums)/2) :
                print(key,value)
                max_number=value
                res=key

        return res

        
                
                