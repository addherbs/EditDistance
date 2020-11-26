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


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums) - 1)
    
    def helper(self, nums, left, right):
        
        if left == right: return nums[left]
        
        mid = left + (right - left) // 2
        
        left_sum = self.helper(nums, left, mid)
        right_sum = self.helper(nums, mid + 1, right)
        cross_sum = self.cross_sum(nums, left, right, mid)
        
        return max(left_sum, right_sum, cross_sum)
    
    def cross_sum(self, nums, left, right, mid):
        if left == right: return nums[left]
        
        left_sub_sum = float('-inf')
        left_sum = 0
        for i in range(left, mid + 1):
            left_sum += nums[i]
            left_sub_sum = max(left_sum, left_sub_sum)
        
        print(left, mid, right)
        print ("LEFT, ", nums[left: mid+1], left_sub_sum)
        
        left_sub_sum = float('-inf')
        left_sum = 0
        for i in range(mid, left - 1, -1):
            left_sum += nums[i]
            left_sub_sum = max(left_sum, left_sub_sum)
            
        print ("Left, ", nums[left: mid+1], left_sub_sum)
        print("$" * 50)
        
        right_sub_sum = float('-inf')
        right_sum = 0
        for i in range(mid + 1, right + 1):
            right_sum += nums[i]
            right_sub_sum = max(right_sum, right_sub_sum)
        
        return left_sub_sum + right_sub_sum