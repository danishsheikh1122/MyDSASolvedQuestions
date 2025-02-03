class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a,b=int(a,2),int(b,2)
        while b:
            temp_wc=a^b
            temp_c=(a&b)<<1
            a,b=temp_wc,temp_c
        return bin(a)[2:]

        