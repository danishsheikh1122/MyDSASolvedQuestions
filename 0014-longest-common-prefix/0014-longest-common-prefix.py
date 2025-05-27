class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # min_str=float("inf")
        # for s in strs:
        #     min_str=min(min_str,len(s))
        # i=0
        # while i < min_str:
        #     for s in strs:
        #         if s[i]!=strs[0][i]:#this strs[0][i] will compare all strings in strs with index i 
        #             return s[:i]
        #     i+=1
        # return s[:i]

        # # greg hog
        min_len=min(len(s) for s in strs)
        i=0
        while i < min_len:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i+=1
        return strs[0][:i]








