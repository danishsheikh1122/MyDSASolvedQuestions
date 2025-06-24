class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # --------------------------------------
        # # check len
        # if len(s)!=len(t):
        #     return False
        # di={}
        # for i in range(len(s)):
        #     if s[i] not in di and t[i] not in di: 
        #         di[s[i]]=t[i]
        #     elif di[s[i]]==t[i]:
        #         continue
        #     else:
        #         return False
        # return True
        # FAILED39/46 
        # -------------------------------------------
        # use 2 dic for forward and reverse mapping 
        if len(s)!=len(t):
            return False
        dist,dits={},{}
        for i in range(len(s)):
            c1,c2=s[i],t[i]
            if ((c1 in dist and dist[c1]!=c2) or (c2 in dits and dits[c2]!=c1)):
                return False
            dist[c1]=c2
            dits[c2]=c1
        return True

                                                                      
