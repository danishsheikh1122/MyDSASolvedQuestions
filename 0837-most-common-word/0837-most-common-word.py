# class Solution(object):
#     def mostCommonWord(self, p, banned):
#         """
#         :type paragraph: str
#         :type banned: List[str]
#         :rtype: str
#         """

#         special_chars = "!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/~"
#         for char in special_chars:
#             p = p.replace(char, ' ')
#         print(p)
#         # below step can be simplified
#         # p=p.split(' ')
#         # p=[c.lower() for c in p]
#         p=p.lower().split()
#         di=Counter(p)
#         print(di)

#         banned.append('')
#         for word in banned:
#             del di[word]

#         # di=dict(sorted(di.items(), key=lambda item: item[1]))
#         # print(di)
#         # not working

#         maxx=0
#         ans=''
#         for key,value in di.items():
#             if maxx<value:
#                 maxx=value
#                 ans=key
#         return ans
#         # worst solution 
#         # TC on 
#         # SC on
from collections import Counter

class Solution(object):
    def mostCommonWord(self, p, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        # Remove specific special characters
        for char in "!?',;.":
            p = p.replace(char, ' ')
        
        # Convert to lowercase and split into words
        p = p.lower().split()
        
        # Count the frequency of each word
        di = Counter(p)
        
        # Remove banned words
        for word in banned:
            if word in di:
                del di[word]
        
        # Find the most common word
        max_count = 0
        ans = ''
        for key, value in di.items():
            if value > max_count:
                max_count = value
                ans = key
                
        return ans
