"""
3Sum

Solution
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            
            target = -nums[i]
            low, hi = i + 1, len(nums) - 1
            
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                
                while low < hi:
                    add = nums[low] + nums[hi] 
                    if add < target:
                        low += 1
                    elif add > target:
                        hi -= 1
                    else:
                        ans.append([nums[i], nums[low], nums[hi]])
                        low += 1
                        hi -= 1
                        while low < hi and nums[low] == nums[low-1]:
                            low += 1
        
        return ans


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = set()
        outer_set, inner_set = set(), dict()
        
        for i, val in enumerate(nums):
            if val not in outer_set:
                outer_set.add(val)
                target = -val
                
                for j, value in enumerate(nums[i+1:]):
                    if target - value in inner_set and inner_set[target-value] == i:
                        result.add(tuple(sorted([val, value, target-value])))
                    inner_set[value] = i
        return result                