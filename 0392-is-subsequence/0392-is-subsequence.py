class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s=="":
            return True
        ptr=0

        for i in range(len(t)):
            if s[ptr]==t[i]:
                if len(s)-1==ptr:
                    return True
                ptr+=1
        return False