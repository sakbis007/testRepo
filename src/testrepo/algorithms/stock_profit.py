"""Best Time to Buy and Sell Stock — find the maximum single-transaction profit."""


def max_profit_brute(prices: list) -> int:
    """O(n²) time — compare every pair."""
    best = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            best = max(best, prices[j] - prices[i])
    return best


def max_profit_linear(prices: list) -> int:
    """O(n) time, O(1) space — track running minimum."""
    min_price = float("inf")
    best = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            best = max(best, price - min_price)
    return best


def max_profit_kadane(prices: list) -> int:
    """O(n) time, O(1) space — Kadane's algorithm on daily deltas."""
    max_gain = current_gain = 0
    for i in range(1, len(prices)):
        current_gain = max(0, current_gain + prices[i] - prices[i - 1])
        max_gain = max(max_gain, current_gain)
    return max_gain
