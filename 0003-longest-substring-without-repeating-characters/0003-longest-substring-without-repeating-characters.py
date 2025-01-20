
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # passes 407/1000
        # res_s=""
        # max_len=0
        # for char in s:
        #     if char not in res_s:
        #         res_s+=char
        #         max_len=max(max_len,len(res_s))
        #     else:
        #         res_s=""
        #         res_s+=char
        # return max_len
        
        # -----------------------------------------
        # sliding window approach 

        max_len=l=r=0
        di={}

        while r<len(s):

            if s[r] in di:
                if di[s[r]]>=l:
                    l=di[s[r]]+1
            
            max_len=max(max_len,r-l+1)
            di[s[r]]=r
            r+=1
        print(di,max_len)
        return max_len


