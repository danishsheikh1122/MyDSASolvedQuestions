class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        first count the no of bollons and store in hash map 

        """
        di=defaultdict(int)

        strr=set('balloon')

        for char in text:
            if char in strr:
                di[char]+=1
        print(di)
        

        return min(di['b'],di['a'],di['l']//2,di['o']//2,di['n'])
        