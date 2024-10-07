class Solution(object):
    def rotate(self, m):
        """
        :type m: List[List[int]]
        :rtype: None Do not return anything, modify m in-place instead.
        """
        # Brute force on2+extra space
        # li=[[0 for i in range(len(m[0]))] for x in range(len(m))]
        # for i in range(len(m)):
        #     for j in range(len(m)):
        #         li[j][i-len(m)-1]=m[i][j]
        
        # print(li)
        # wrong
        # ----------------------------------

        for i in range(0,len(m)):
            # here we are using i,len(m) to just traverse top half portion of the arrat 
            for j in range(i,len(m)):
                print(i,j)
                temp=m[i][j]
                m[i][j]=m[j][i]
                m[j][i]=temp
                
                # if i==j:
                #     continue
                # else:
                #     temp=m[i][j]
                #     m[j][i]=temp
                #     m[j][i]=m[i][j]
        print(m)
        for i in range(len(m)):
            m[i].reverse()



