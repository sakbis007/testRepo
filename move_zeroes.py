from typing import List


class Solution:
    def move_zero(self, nums: List[int]) -> None:
        # Two-pointer: `insert` marks where the next non-zero goes.
        # O(n) time, O(1) space. Modifies nums in place.
        insert = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert], nums[i] = nums[i], nums[insert]
                insert += 1


if __name__ == "__main__":
    sol = Solution()
    arr = [0, 1, 0, 3, 12]
    sol.move_zero(arr)
    print(arr)  # [1, 3, 12, 0, 0]
