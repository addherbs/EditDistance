"""
46. Permutations
Medium

4747

115

Add to List

Share
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) == 1:
            return [[nums[0]]]
        if nums:
            first = [nums[0]]
            for each in self.permute(nums[1:]):
                # print (each)
                for index in range(len(each)+1):
                    ans.append(each[:index] + first + each[index:])

        return ans