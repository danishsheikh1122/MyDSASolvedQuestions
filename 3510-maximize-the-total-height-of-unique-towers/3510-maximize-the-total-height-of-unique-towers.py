class Solution(object):
    def maximumTotalSum(self, h):
#         """
#         :type h: List[int]
#         :rtype: int
#         use a di or counter to identify dups
#         if then..
#         else
#         return sum
#         """
#         from collections import Counter
#         di=Counter(h)
#         t_h=0
        

#         def reducee(k,v):
#             if(v>0):
#                 print(di)
#                 di[k]-=1
#                 # if(k-)
#                 k-=1
#                 di[k]=di[k]+1 if k in di else 1

#             return 

#         def callitself():
#             for key,value in di.items():
#                 if(value>=2):
#                     reducee(key,value)
#                     print(di)
#                     callitself()
#         callitself()
        

#         for key,value in di.items():
#             if(value<=1 and key!=0):
#                 t_h+=key
#             else:
#                 return -1
#         return t_h


# # [2,3,4,3]
# # [15,10]
# # [2,2,1]
        h.sort(reverse=True)
        ans = 0
        cur = h[0]
        for height in h:
            if cur == 0:
                return -1
            if cur > height:
                cur = height
            ans += cur
            cur -= 1
        return ans
            
        