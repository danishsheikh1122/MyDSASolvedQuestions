class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # res_str=""
        # i=l=r=0
        # l1=len(word1)
        # l2=len(word2)
        # while i<min(l1,l2):
        #     res_str+=word1[l]
        #     res_str+=word2[r]
        #     l+=1
        #     r+=1
        #     i+=1

        # res_str=res_str+word1[l:] if l1>l2 else res_str+word2[r:] 
        # print(res_str)
        # return res_str
        
        min_len=min(len(word1),len(word2))
        new_str=""
        for i in range(min_len):
            new_str+=word1[i]
            new_str+=word2[i]
        new_str+=word1[min_len:] if len(word1)>len(word2) else word2[min_len:]
        # print(new_str)
        return new_str






