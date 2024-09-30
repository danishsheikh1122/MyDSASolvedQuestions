class Solution(object):
    def shortestCompletingWord(self, lp, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
         
        """
        
        min_len_word=float('inf')
        res_str=''
        lp=lp.lower()

        di={}
        li=[]
        total=0
        toremove=['0','1','2','3','4','5','6','7','8','9',' ']
        for c in lp:
            if c not in toremove:
                di[c]=di[c]+1 if c in di else 1
                total+=1
        di_cpy=di.copy()
        print(di_cpy)
        for w in words:
            temp=len(w)
            i=0
            for c in w:
                # print(c)
                if c in di_cpy and di_cpy[c]>=1 :
                    # print('in')
                    di_cpy[c]-=1

                    i+=1
                if c in di_cpy and di_cpy[c]==0:
                    print(di_cpy)
                    del di_cpy[c]

                if i==total:
                    # if min_len_word>temp :
                    #     # print(i,temp,w)
                    #     min_len_word=temp
                    #     res_str=w
                    # elif min_len_word<temp and min :
                    #     min_len_word=temp
                    #     res_str=w
                    li.append(w)

                    

            di_cpy=di.copy()
        print(di_cpy,li)
        # print(min(li,key=len))
        return min(li,key=len)


        # worst code i ever wrote 