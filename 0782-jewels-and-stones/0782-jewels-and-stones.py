class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        count a char
        and then store it in dict key=key and value =count

        """
        # best solution to look into a dict hashmap it only takes o(1) tc
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
        # -------------------

        # this approach uses only str functions
        # res=0
        # for char in stones:
        #     if char in jewels:
        #         res+=1
        # return res

        # tc-sc->O(n*m) little bit slower

#---------------------------------------------
        jewels=set(jewels)
        res=0
        for char in stones:
            if char in jewels:
                res+=1
        return res