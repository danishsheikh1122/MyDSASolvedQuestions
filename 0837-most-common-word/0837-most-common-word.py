class Solution(object):
    def mostCommonWord(self, p, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        special_chars = "!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/~"
        for char in special_chars:
            p = p.replace(char, ' ')
        print(p)
        p=p.split(' ')
        p=[c.lower() for c in p]
        di=Counter(p)
        print(di)

        banned.append('')
        for word in banned:
            del di[word]

        # di=dict(sorted(di.items(), key=lambda item: item[1]))
        # print(di)
        # not working

        maxx=0
        ans=''
        for key,value in di.items():
            if maxx<value:
                maxx=value
                ans=key
        return ans
        