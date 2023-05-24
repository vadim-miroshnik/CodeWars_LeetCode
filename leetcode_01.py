# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        for i1 in range(0, len(nums)):
            for i2 in range(i1 + 1, len(nums)):
                for i3 in range(i2 + 1, len(nums)):
                    if nums[i1] + nums[i2] + nums[i3] == 0:
                        __exist = False
                        for row in result:
                            if sorted(row) == sorted([nums[i1], nums[i2], nums[i3]]):
                                __exist = True
                                break
                        if not __exist:
                            result.append([nums[i1], nums[i2], nums[i3]])
        return result


sol = Solution()
res = sol.threeSum([-1, 0, 1, 2, -1, -4])
print(res)
res = sol.threeSum([0, 1, 1])
print(res)
res = sol.threeSum([0, 0, 0])
print(res)
