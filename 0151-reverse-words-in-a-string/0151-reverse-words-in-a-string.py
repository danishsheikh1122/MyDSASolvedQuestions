class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # works
        # arr=s.split()
        # arr.reverse()
        # strr=""
        # for w in arr:
        #     strr+=w
        #     if w!=" " and w!=arr[-1]:
        #         strr+=" "
        # return strr
        

        # brute force using stack
        stack=[]
        for word in s.strip().split():#use strip before split
            if word:
                stack.append(word)
        reverseWords=[]

        while stack:
            reverseWords.append(stack.pop())
        
        return " ".join(reverseWords)


