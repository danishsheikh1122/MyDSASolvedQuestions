class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        create a counter and count every word and just check if every char is   
        present or not 
        """
        counter={}
        for char in s:
            counter[char]=counter[char]+1 if char in counter else 1
        if len(s)!=len(t):
            return False
        for char in t:
            if char not in counter:
                return False
            elif counter[char]==1:
                del counter[char]
            else:
                counter[char]-=1
        return True
            
                

        