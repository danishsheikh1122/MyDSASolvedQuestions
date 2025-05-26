class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s=="":
            return True
        # ptr=0

        # for i in range(len(t)):
        #     if s[ptr]==t[i]:
        #         if len(s)-1==ptr:
        #             return True
        #         ptr+=1
        # return False

        # # on o1



        i=lenn=0
        for char in t:
            if s[lenn]==char:
                lenn+=1
                if lenn==len(s):
                    return True
            i+=1
        
        return False





