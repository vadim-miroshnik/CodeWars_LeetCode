# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum_1(self, nums: list[int]) -> list[list[int]]:
        """ first approach -Time Limit Exceeded"""
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

    def threeSum_2(self, nums: list[int]) -> list[list[int]]:
        """ second approach -Two Pointers"""
        result = []
        nums.sort()
        for i, val in enumerate(nums):
            if val > 0:  # lowest number already bigger than 0
                break
            if i > 0 and nums[i] == nums[i-1]:  # skip equal numbers
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum3 = val + nums[left] + nums[right]
                if sum3 > 0:
                    right -= 1  # make sum smaller by moving right pointer
                elif sum3 < 0:
                    left += 1  # make sum bigger by moving left pointer
                else:
                    result.append([val, nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while nums[left] == nums[left-1] and left < right:  # skip equal numbers
                        left += 1
        return result


sol = Solution()
res = sol.threeSum_2([-1, 0, 1, 2, -1, -4])
print(res)
res = sol.threeSum_2([0, 1, 1])
print(res)
res = sol.threeSum_2([0, 0, 0])
print(res)
