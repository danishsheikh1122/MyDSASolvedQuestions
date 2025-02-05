class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res_str=""
        max_len=0
        for i in range(len(s)):
            l=r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>max_len:

                    res_str=s[l:r+1]
                    max_len=(r-l+1)
                l-=1
                r+=1       
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>max_len:

                    res_str=s[l:r+1]
                    max_len=(r-l+1)
                l-=1
                r+=1

        return res_str



            

        