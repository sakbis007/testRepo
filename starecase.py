# Problem: You're climbing a staircase with n steps. Each time you can climb either 1 or 2 steps. 
# In how many distinct ways can you reach the top?

#Solution 1 — Recursion O(2ⁿ) (Slow)
from datetime import datetime


def climb_stairs(n):
    if n <= 2:
        return n
    return climb_stairs(n-1) + climb_stairs(n-2)

#Solution 2 — Memoization O(n) (Top-Down DP)
def climb_stairs_2(n,memo={}):
    if n <=2:
        return n
    if n in memo:
        return memo[n]
    memo[n] = climb_stairs_2(n-1,memo) + climb_stairs_2(n-2,memo)
    return memo[n]
# Example usage:
if __name__ == "__main__":
    print(datetime.now())
    print(climb_stairs(35))
    print(datetime.now())

    print(climb_stairs_2(50))
    print(datetime.now())