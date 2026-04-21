# Problem: Given an array prices where prices[i] is the price of a stock on day i, 
# find the maximum profit you can achieve by buying on one day 
# and selling on a later day. If no profit is possible, return 0. 
# You can only make one transaction (one buy + one sell).


# time complexity: O(n^2)
def max_profit(prices):
    max_profit=0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            profit=prices[j]-prices[i]
            max_profit=max(max_profit,profit)
    return max_profit

# time complexity: O(n)
def max_profit_optimized(prices):
    min_price = float('inf') # Initialize min_price to a very large value
    res = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            res = max(res, price - min_price)

    return res

# time complexity: O(n) and space complexity: O(1) Kadane's Approach
def max_profit_kadane(prices):
    max_gain = 0
    current_gain = 0

    for i in range(1, len(prices)):
        current_gain += prices[i] - prices[i - 1]
        if current_gain < 0:
            current_gain = 0
        max_gain = max(max_gain, current_gain)

    return max_gain
if __name__=="__main__":
    prices=[1,10,2,13]
    print(max_profit(prices)) 
    print(max_profit_optimized(prices))  # Output: 8 (Buy on day 2 and sell on day 3)
    print(max_profit_kadane(prices))  # Output: 8 (Buy on day 2 and sell on day 3)