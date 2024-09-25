class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        make a dict and count all even elements 
        and take out all max in li and then return it 
        and if 2 values has same count then return min 
        return -1 i not any
        """
        di=defaultdict(int)
        for i in nums:
            if(i%2==0):
                di[i]+=1
        print(di)
        
        max_value=0
        min_key=-1       
        for key,value in di.items():
            if(value>max_value):
                max_value,min_key=value,key
                print(max_value)
            elif( max_value==value):
                min_key=min(min_key,key)
        return min_key
                
