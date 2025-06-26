class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # di = Counter(s)  
        # dii = sorted(di.items(), key=lambda item: (-item[1],item[0])) 
        # print(dii)

        # new_str = ""
        # for key, value in dii:
            # new_str += key * value 
        # return new_str
        di=Counter(s)
        di=sorted(di.items(),key=lambda item:(-item[1],item[0]))
        resStr=""
        for key,value in di:
            resStr+=key*value
        return resStr
        













