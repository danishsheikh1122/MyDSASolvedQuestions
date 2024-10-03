class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(0,9):
            check_dups=set()
            # print(i)
            for j in range(0,9):
                temp=board[i][j]
                if temp in check_dups:
                    return False
                elif temp is not '.':
                    check_dups.add(temp)

                    

        for i in range(0,9):
            check_dups=set()
            # print(i)
            for j in range(0,9):
                temp=board[j][i]
                if temp in check_dups:
                    return False
                elif temp is not  '.':
                    check_dups.add(temp)


        to_iterate=[(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]

        for i,j in to_iterate:
            sett=set()
            for row in range(i,i+3):#exclusive
                for column in range(j,j+3):
                    if board[row][column] in sett :
                        return False
                    # elif board[row][column] not in ".":
                    elif board[row][column] is not ".":
                        sett.add(board[row][column])


        return True