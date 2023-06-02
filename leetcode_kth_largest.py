# 215. Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.
# Example 1: Input: nums = [3,2,1,5,6,4], k = 2,  Output: 5
# Example 2: Input: nums = [3,2,3,1,2,4,5,5,6], k = 4,  Output: 4
# https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest1(self, nums: list[int], k: int) -> int:
        """ O log n solution"""
        nums.sort()
        return nums[len(nums) - k]

    def findKthLargest2(self, nums: list[int], k: int) -> int:
        """ O(n) solution (average)"""
        kInd = len(nums) - k

        def quickSelect(left, right):
            pivot, pointer = nums[right], left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1
            nums[pointer], nums[right] = nums[right], nums[pointer]
            if pointer > kInd:
                return quickSelect(left, pointer - 1)
            elif pointer < kInd:
                return quickSelect(pointer + 1, right)
            else:
                return nums[pointer]

        return quickSelect(0, len(nums) - 1)


sol = Solution()

res = sol.findKthLargest2([3, 2, 1, 5, 6, 4], 2)
print(res)

res = sol.findKthLargest2([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
print(res)

