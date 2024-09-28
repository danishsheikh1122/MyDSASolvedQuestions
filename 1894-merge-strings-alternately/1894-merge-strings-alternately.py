class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # s=word2[:len(word1)]
        minW=word1 if len(word1)<len(word2) else word2
        maxW=word1 if len(word1)>len(word2) else word2
        l=len(minW)
        print(l)

        resS=""
        r=0
        while r!=l:
            resS=resS+word1[r]+word2[r]
            r+=1
        resS+=maxW[r:]
        return resS

            

        
        