# from collections import Counter

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
