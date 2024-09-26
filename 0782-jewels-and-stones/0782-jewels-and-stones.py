class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        count a char
        and then store it in dict key=key and value =count

        """
        # my own solution 
        # di={}
        # for char in jewels:
        #     di[char]=0

        # for char in stones:
        #     if char in di:
        #         di[char]+=1   
        # res=0

        # for key,value in di.items():
        #     res+=value
    
        # return res

        # tc&sc->o(n+m)

        res=0
        for char in stones:
            if char in jewels:
                res+=1
        return res

