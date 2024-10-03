class Solution(object):
    def checkValid(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        l=len(m)

        for i in range(0,l):
            sett=set()
            for j in range(0,l):
                if m[i][j] in sett:
                    return False
                else:
                    sett.add(m[i][j])


        for i in range(0,l):
            sett=set()
            for j in range(0,l):
                if m[j][i] in sett:
                    return False
                else:
                    sett.add(m[j][i])

        
        return True