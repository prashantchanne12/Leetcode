directions = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, 1), (1, 2), (2, -1), (1, -2)]

def knight_probability(n, k, row, col):
    
    dp = [[[0 for x in range(k+1)] for y in range(n)] for z in range(n)]
    

    return knight_probability_recursive(n, k, row, col, dp)

def knight_probability_recursive(n, k, row, col, dp):
    
    if row >= n or row < 0 or col >= n or col < 0:
        return 0
        
    if k == 0:
        return 1
    
    
    if dp[k][row][col] != 0:
        return dp[k][row][col]
        
    res = 0
    
    for r, c in directions:
        res += knight_probability_recursive(n, k-1, row+r, col+c, dp) / 8
        
    dp[k][row][col] = res
    
    return dp[k][row][col]
    

print(knight_probability(3, 2, 0, 0))
    