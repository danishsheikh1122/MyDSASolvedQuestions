class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        m_freq=max_len=l=r=0
        di={}  
        while r<len(s):
            if not s[r] in di:
                di[s[r]]=0
            di[s[r]]+=1

            if (r-l+1)-max(di.values())<=k:
                max_len=max(max_len,r-l+1)
            else:
                di[s[l]]-=1
                if not di[s[l]]:
                    di.pop(s[l])
                l+=1
            r+=1
        return max_len
