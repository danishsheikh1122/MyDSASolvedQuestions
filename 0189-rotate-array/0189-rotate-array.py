class Solution(object):
    def rotate(self, n, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        # """

        # # brute force 
        # temp=n[len(n)-1]
        # for i in range(0,len(n)):
        #     for j in range(count,len(n)):
        #         count

        # li=[0]*len(n)
        # # print(li)
        # temp=0
        # for i in range(k,len(n)):
        #     li[i]=n[temp]
        #     temp+=1
        # # print(li)
        # if(len(n)%2!=0 and len(n)!=1) :
        #     temp=0
        #     for i in range(k+1,len(n)):
        #         li[temp]=n[i]
        #         temp+=1
        #     # print(li)
        # else:
        #     temp=0
        #     for i in range(k,len(n)):
        #         li[temp]=n[i]
        #         temp+=1
        # # print(li)

        # for i in range(len(n)):
        #     n[i]=li[i]


        # -------------------------------------
        # PASSES 34/38 GOOD SOLUTION BUT TLE 
        # if len(n)==1:
        #     return n

        # l=len(n)-1
        # while k!=0:
        #     temp=n[0]
        #     n[0]=n[l]
        #     print(n[l])

        #     for i in range(l,1,-1):
        #         n[i]=n[i-1]
                
        #     n[1]=temp

        #     k-=1

        #     print(n)
        # -------------------------------------


        # if len(n)==1:
        #     return n

        # to reduce rotations 
        # if we rotate  arr of len 3 - 3 times then we'll be getting the same arr
        # so we're reducing the rotation count

        # k=k%len(n)
        # temp=n[:k]

        # for i in range(k,len(n)):
        #     n[i-k]=n[i]
        # print(n)

        # for i in temp:
        #     n[k]=i
        #     k+=1


        # again wrong
        # -------------------------

        if len(n)==1:
            return n

        k = k % len(n)      
        temp_len = len(n) - k
        # Store the elements to move
        temp = n[0:temp_len]
        print(temp)
        # Remove the elements from the beginning
        n[0:temp_len] = []
        print(n)
        # Append the stored elements to the end
        n.extend(temp)
        print(n)


        