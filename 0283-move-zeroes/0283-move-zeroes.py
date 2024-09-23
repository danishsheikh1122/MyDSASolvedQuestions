class Solution(object):
    def moveZeroes(self, n):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #worst approach
        # arr_len=len(n)-1
        # new_li=[x for x in n if x!=0]
        # # print(new_li)
        # for i in range(len(new_li)-1,arr_len):
        #     new_li.append(0)
        # # print(new_li)

        # for i in range(0,len(new_li)):
        #     n[i]=new_li[i]


        count_zeros=0
        move_backward=0

        for i in range(len(n)):
            if n[i]!=0:
                n[move_backward]=n[i]
                move_backward+=1
            else:
                count_zeros+=1
        k=move_backward-1      
        i=len(n)-1
        while k!=i:
            n[i]=0
            i-=1
        print(n)