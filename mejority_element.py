from typing import List


class Solution:
    def mejorityElement(self, nums: List[int]) -> int:
        # Approach 1: Boyer-Moore Voting -> O(n) time, O(1) space (optimal)
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

    def mejorityElement_dict(self, nums: List[int]) -> int:
        # Approach 2: Manual hash map count -> O(n) time, O(n) space
        counts = {}
        n = len(nums)
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > n // 2:
                return num
        return -1

    def mejorityElement_bits(self, nums: List[int]) -> int:
        # Approach 3: Bit manipulation -> O(32n) time, O(1) space
        n = len(nums)
        result = 0
        for bit in range(32):
            bit_count = 0
            for num in nums:
                if (num >> bit) & 1:
                    bit_count += 1
            if bit_count > n // 2:
                result |= 1 << bit
        # handle negative numbers (two's complement, 32-bit)
        if result >= 2 ** 31:
            result -= 2 ** 32
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.mejorityElement_dict([2, 2, 1, 1, 1, 2, 2]))