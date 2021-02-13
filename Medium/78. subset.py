"""
78. Subsets
Medium

4667

93

Add to List

Share
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = [each for each in self._recurse(nums)]
        if ans:
            ans.append([])
        return ans
        
        
    def _recurse(self, nums):
        ans = []
        if nums:
            ans.append([nums[0]])

            for each in self._recurse(nums[1:]):
                ans.append(each)
                ans.append([nums[0]] + each)

        return ans