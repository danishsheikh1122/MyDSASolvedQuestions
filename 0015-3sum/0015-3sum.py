class Solution(object):
    def threeSum(self, n):
        """
        :type n: List[int]
        :rtype: List[List[int]]
        """
        # brute force
        # res = set()


        # for i in range(len(n)):
        #     for j in range(i + 1, len(n)):
        #         for k in range(j + 1, len(n)):
        #             if n[i] + n[j] + n[k] == 0:
        #                 li = tuple(sorted([n[i], n[j], n[k]]))
        #                 res.add(li)

        # return res

        # ------------------------------------------------
        # Using 2 ptr approach most optimal one 

        # i is normal ptr and j,k is l anr r resp
        n.sort()
        res=set()
        for i in range(0,len(n)):
            l=i+1
            r=len(n)-1
            # this if makes code faster if i ==i-1 then same number so move to non similar number 
            if i>0 and n[i]==n[i-1]:
                continue
            while l<r:
                isZero=n[i]+n[l]+n[r]

                if isZero==0:
                    res.add((n[i],n[l],n[r]))
                    l+=1
                    r-=1

                    # this 2 while loops makes the code fast 
                    # if same elem appear then it will jumn to next non similar  number
                    while l<r and n[l]==n[l-1]:
                        l+=1
                    while l<r and n[r]==n[r+1]:
                        r-=1
                elif isZero<0:
                    l+=1
                else:
                    r-=1
        return list(res)



