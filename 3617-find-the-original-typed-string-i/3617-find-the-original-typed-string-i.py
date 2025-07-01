class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        # di=Counter(word)
        # print(di)
        # count=0
        # for key,value in di.items():
        #     if value-1==0:
        #         continue
        #     count+=(value-1)
        
        # return count


        count=1
        for i in range(len(word)-1):
            if word[i]==word[i+1]:
                count+=1
        return count
 
            
        