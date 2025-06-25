class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # wrong code
        # for i in range(len(s)):
        #     first=s[0]
        #     for j in range(0,len(s)):
        #         s[j]=s[j+1]
        #     s[-1]=first
        #     if s==goal:
        #         return true
        # return false
        # ------------------------------------
        # just combine 2 str and check if goal is present in new_str
        # if true return true else false 
        # as simple as fuck w
        if len(s)!=len(goal):
            return False
        s=s+s
        return True if goal in s else False


        