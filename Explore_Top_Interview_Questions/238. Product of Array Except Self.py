"""
238. Product of Array Except Self
Medium

6203

488

Add to List

Share
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums: return nums
        
        n = len(nums)
        ans = [0] * (n)
        ans[0] = 1 if nums[0] else 0
        ans[-1] = 1 if nums[-1] else 0
        
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        
        prod = nums[-1]
        for i in range(n-2, -1, -1):
            ans[i] = ans[i] * prod
            prod = prod * nums[i]
        
        return ans