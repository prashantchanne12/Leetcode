def rod_cutting(length, price, n):
    dp = [[0 for _ in range(n+1)] for _ in range(len(length)+1)]
    
    for i in range(1, len(length) + 1):  # Iterate over available lengths
        for j in range(1, n + 1):  # Iterate over the rod length
        
            if length[i - 1] <= j:
                # Either we don't cut at this length OR we cut (unbounded behavior)
                dp[i][j] = max(dp[i - 1][j], price[i - 1] + dp[i][j - length[i - 1]])
            else:
                # If we can't cut at this length, take the previous best value
                dp[i][j] = dp[i - 1][j]
                
    return dp[len(length)][n]  # Return the max profit from the last cell
            
length = [1, 2, 3, 4, 5, 6, 7, 8]
price = [1, 5, 8, 9, 10, 17, 17, 20]
N = 8
print(rod_cutting(length, price, N))  # Expected output: 22
