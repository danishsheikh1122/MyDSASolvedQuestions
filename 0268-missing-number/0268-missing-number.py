class Solution(object):
    def missingNumber(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force worst solution posible

        # minn=0
        # maxx=max(n)+1

        # for i in range(maxx+1):
        #     if(i not in n):
        #         return i
        # return 0
        # TC=O^2
        # SC=O(1)

# ----------------------------
# passed 110/122 great

        # sort arr first
        # the run a loop if diff between i and i+1==1 continue
        # else :
        #     return i

        # n.sort()
        # move_backward=0
        # for i in range(1,len(n)):
        #     if(abs(n[move_backward]-n[i])==1):
        #         move_backward+=1
        #         continue
        #     else:
        #         return i
        # if(len(n)!=1):        
        #     return len(n)
        # else:
        #     for i in range(0,len(n)+1):
        #         if(abs(n[move_backward]-n[i])==1):
        #             move_backward+=1
        #             continue
        #         else:
        #             return i


# -------------------------------------
# using a formula to calc sum as
# sum of n numbers = (n(n+1))/2
        lenn=len(n)
        res=(lenn*(lenn+1)) // 2
        summ=sum(n)
        return res-summ