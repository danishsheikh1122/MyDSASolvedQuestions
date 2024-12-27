class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        di={}
        for c in s:
            di[c]=di[c]+1 if c in di else 1
        print(di)
        for c in t:
            if c in di and di[c]>0:
                di[c]-=1
            else:
                return False
        
        return True