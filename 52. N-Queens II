class Solution:
    def totalNQueens(self, n: int) -> int:
        ans=[]
        board=[['.']*(n) for i in range(n)]
        def isValid(row,col):
            rn=row
            cn=col
            #column
            for i in range(n):
                if board[i][col]=='Q' and i!=row:
                    return False
            #upright
            r=rn-1
            c=cn-1
            while r>=0 and c>=0:
                if board[r][c]=='Q':
                    return False
                r-=1
                c-=1
            r=rn-1
            c=cn+1
            while r>=0 and c<n:
                if board[r][c]=='Q':
                    return False
                r-=1
                c+=1
            return True
        def helper(board,rn,cn):
            if rn>=n:
                temp=[''.join(board[i]) for i in range(n)]
                ans.append(temp)
                return
            for i in range(n):
                board[rn][i]='Q'
                if isValid(rn,i):
                    helper(board,rn+1,i)
                board[rn][i]='.'
        helper(board,0,0)
        return len(ans)
