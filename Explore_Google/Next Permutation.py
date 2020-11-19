"""
Next Permutation

Solution
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        val, next_min = 0, 0
        i = len(nums)-1
        
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        if i > 0 and nums[i-1] < nums[i]:
            val = nums[i-1]
            next_min = nums[i]
            j = i + 1
            swap_index = i
            while j < len(nums):
                if nums[j] != val:
                    if nums[j] <= next_min and nums[j] > val:
                        next_min = nums[j]
                        swap_index = j
                j += 1
            nums[i-1], nums[swap_index] = nums[swap_index], nums[i-1]
        j = len(nums) - 1
        while i < j and nums[i] >= nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        