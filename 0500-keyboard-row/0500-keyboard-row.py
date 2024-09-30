class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        bruteforce is to create 3 str and check if arr belongs to anyone 
        else

        """
        
        di={1:'qwertyuiop',
            2:'asdfghjkl',
            3:'zxcvbnm'}
        res_li=[]
        index=0
        for w in words:
            w=[x.lower() for x in w]
            
            row=0
            if w[0] in di[1]:
                row+=1
            elif w[0] in di[2]:
                row+=2
            elif w[0] in di[3]:
                row+=3
            l=len(w)
            i=0
            # for char in w:
            #     # print(row)
            #     if char in di[row]:
            #         i+=1
            #     if(i == l):
            #         # print(i,l)
            #         res_li.append(words[index])
            if all(char in di[row] for char in w):
                res_li.append(words[index])

            index+=1

        # print(res_li)
        return res_li
        # TC ON2 or O n * k
        # SC ON
        # beats 89 tms and 99 on s