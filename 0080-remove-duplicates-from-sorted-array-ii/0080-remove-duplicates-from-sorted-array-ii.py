class Solution(object):
    def removeDuplicates(self, n):
        """
        :type n: List[int]
        :rtype: int
        """
        count=1
        j=1
        # take len (n) in a var coz size of n will change
        l=len(n)
        for i in range(1,l):
            if n[i]==n[i-1]:
                count+=1
            else:
                count=1

            if count<=2:
                n[j]=n[i]
                j+=1
        return j         