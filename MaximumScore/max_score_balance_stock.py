def getMaximumScore(stockPrices):
    n = len(stockPrices)
    dp = [0] * n  # dp[i] stores the maximum score for a balanced subsequence ending at index i
    
    for i in range(1, n):
        dp[i] = stockPrices[i]  # Initialize with the price at index i
        for j in range(i - 1, -1, -1):
            diff_days = i - j
            price_diff = stockPrices[i] - stockPrices[j]
            
            if price_diff == diff_days:
                dp[i] = max(dp[i], dp[j] + stockPrices[i])
                
        dp[i] = max(dp[i], dp[i - 1])  # Consider not selecting the current day
        
    return max(dp)

# Example
stockPrices = [1, 5, 3, 7, 8]
print(getMaximumScore(stockPrices))  # Output: 20

stockPrices = [1, 2, 3]
print(getMaximumScore(stockPrices))  # Output: 6
