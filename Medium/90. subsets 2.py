"""
90. Subsets II
Medium

1978

90

Add to List

Share
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = [each for each in self._recurse(sorted(nums))]
        if ans:
            ans.append([])
        return [list(each) for each in set([tuple(temp) for temp in ans]) ]
        
        
    def _recurse(self, nums):
        ans = []
        if nums:
            ans.append([nums[0]])

            for each in self._recurse(nums[1:]):
                ans.append(each)
                ans.append([nums[0]] + each)

        return ans