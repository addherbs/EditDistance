"""
47. Permutations II
Medium

2313

67

Add to List

Share
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        count_dict = Counter(nums)
        answers = []
        self.backtrack([], count_dict, len(nums), answers)
    
        return answers
    
    def backtrack(self, nums, count_dict, total_length, answers):
        
        if total_length == len(nums):
            answers.append(list(nums))
        
        for elem, value in count_dict.items():
            if value > 0:
                nums.append(elem)
                
                count_dict[elem] -= 1
                self.backtrack(nums, count_dict, total_length, answers)
                
                count_dict[elem] += 1
                nums.pop()
                
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        temp = [list(each) for each in set([tuple(temp) for temp in self._recurse(nums)])]
        print (temp)
        return temp
    
    def _recurse(self, nums):
        ans = []

        if len(nums) == 1:
            return [[nums[0]]]

        
        if nums:
            first = [nums[0]]

            for each in self._recurse(nums[1:]):

                for index in range(len(each)+1):
                    ans.append(each[:index] + first + each[index:])
        return ans