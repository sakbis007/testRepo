# Two Sum — Given a list of integers nums and a target integer target, return the indices of the two numbers that add up to target. Assume exactly one solution exists, and you can't use the same element twice.
# Example:
# nums = [2, 7, 11, 15], target = 9 → [0, 1] (because 2 + 7 = 9)
# please solve this problem in python. 1 simple way 2. efficient way
# Simple way (brute force):
def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

# Efficient way (using a hash map):
def two_sum_efficient(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return (num_dict[complement], i)
        num_dict[num] = i
    return None
# main function to test the above implementations
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print("Brute Force Result:", two_sum_brute_force(nums, target))
    print("Efficient Result:", two_sum_efficient(nums, target))