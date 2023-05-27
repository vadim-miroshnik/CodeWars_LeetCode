# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum_1(self, nums: list[int], target: int) -> list[int]:
        """ first approach - O(n3) """
        for i1 in range(0, len(nums)):
            for i2 in range(i1 + 1, len(nums)):
                if nums[i1] + nums[i2] == target:
                    return [i1, i2]

    def twoSum_2(self, nums: list[int], target: int) -> list[int]:
        """ second approach - faster """
        prev = {}  # value - index
        for i, val in enumerate(nums):
            rest = target - val
            if rest in prev:
                return [i, prev[rest]]
            else:
                prev[val] = i
        return


sol = Solution()
res = sol.twoSum_2([5, 25, 75], 100)
print(res)
