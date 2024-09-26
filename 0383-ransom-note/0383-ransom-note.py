class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        to create rn using letters of magazine
        first count the magazine letters 
        create a dict of rn
        and check if magazine has att that chars
        """
        di_r={}
        di_m={}
        for i in ransomNote:
           di_r[i] = di_r[i] + 1 if i in di_r else 1
        for i in magazine:
            if(i in di_r):
                di_m[i] = di_m[i] + 1 if i in di_m else 1

        print(di_r)
        print(di_m)
        res=False
        for key,value in di_r.items():
            if(key in di_m and di_m[key]>=value):
                print(di_m[key])
                res=True
            else:
                return False
        return res



        