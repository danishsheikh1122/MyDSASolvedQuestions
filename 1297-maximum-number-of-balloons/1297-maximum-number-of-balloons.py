class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        s="balloon"
        di=defaultdict(int)
        for c in text:
                di[c]=di[c]+1 if c in di else 1
        return min(di['b'],di['a'],di['l']//2,di['o']//2,di['n'])