class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute fore by me 
        # di=Counter(nums)
        # max_number=0
        # res=0
        # print(di)
        
        # for key,value in di.items():
        #     if value>max_number and value>=(len(nums)/2) :l
        #         print(key,value)
        #         max_number=value
        #         res=key

        # return res
        
        # most optimal solutions can be formed by using moors voting algorithm 
        # how many time you'll revise this danish
        # dumbass 

        current_elem=0
        count=0
        for num in nums:
            if count==0:
                current_elem=num
                count+=1
            elif current_elem==num:
                count+=1
            else:
                count-=1
        return current_elem




        
                
                