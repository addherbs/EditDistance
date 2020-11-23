"""
Maximum Subarray

Solution
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-2147483647]
Output: -2147483647
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
"""


# Space Complexity O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        ans = nums[0]
        temp = [0] * len(nums)
        temp[0] = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] + temp[i-1] > nums[i]:
                temp[i] = nums[i] + temp[i-1]
            else:
                temp[i] = nums[i]
            ans = max(ans, temp[i])

        return ans
        
        
# Space Complexity O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        ans = current_sum = nums[0]

        
        for i in range(1, len(nums)):
            current_sum = max(nums[i], nums[i] + current_sum)
            ans = max(ans, current_sum)

        return ans


