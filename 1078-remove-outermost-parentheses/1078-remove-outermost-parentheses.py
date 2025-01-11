class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans_final=""
        li=[]
        for i in s:
            if i=="(":
                if li:
                    ans_final+=i
                li.append(i)
            elif i==')': 
                    li.pop()
                    if li :
                        ans_final+=i
        return ans_final

        