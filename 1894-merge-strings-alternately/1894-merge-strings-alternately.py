class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # s=word2[:len(word1)]
        # --------------------------------
        # another 2 ptr approach
        # minW=word1 if len(word1)<len(word2) else word2
        # maxW=word1 if len(word1)>len(word2) else word2
        # l=len(minW)
        # print(l)

        # resS=""
        # r=0
        # while r!=l:
        #     resS=resS+word1[r]+word2[r]
        #     r+=1
        # resS+=maxW[r:]
        # return resS

        # Tc on 
        # sc on
        # make it more optimal

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)
            

        
        