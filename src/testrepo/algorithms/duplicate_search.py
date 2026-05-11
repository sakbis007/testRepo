"""Contains Duplicate II — given nums and k, return True if any two distinct
indices i, j satisfy nums[i] == nums[j] and abs(i - j) <= k."""


def dup_search_brute(nums: list, k: int) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
    return False


def dup_search_hash(nums: list, k: int) -> bool:
    """O(n) time, O(k) space — sliding hash map."""
    seen: dict = {}
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False


def dup_search_window(nums: list, k: int) -> bool:
    """O(n) time, O(k) space — explicit sliding window."""
    window: list = []
    for num in nums:
        if num in window:
            return True
        window.append(num)
        if len(window) > k:
            window.pop(0)
    return False
