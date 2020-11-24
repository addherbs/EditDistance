"""
Maximum Product Subarray

Solution
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

# O(N) time complexity
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        
        ans = nums[0]
        max_prod = nums[0]
        min_prod = nums[0]
        
        for i in range(1, len(nums)):
            
            current_max = max(nums[i], max_prod * nums[i], min_prod * nums[i])
            current_min = min(nums[i], max_prod * nums[i], min_prod * nums[i])
            ans = max(ans, current_max)
            
            max_prod = current_max
            min_prod = current_min
            
        return ans