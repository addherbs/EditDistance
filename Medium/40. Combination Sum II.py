# 40. Combination Sum II
#
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]


from collections import Counter


class Solution:
    def combinationSum2(self, candidates, target):
        candidate_map = Counter(candidates)
        result = []
        candidates = list(set(candidates))
        self.cal(candidates, target, result, [], 0, candidate_map)
        return result

    def cal(self, candidates, target, result, current_list, next_index, candidate_map):
        if target == 0:
            result.append(current_list)
            return
        if target < 0 or next_index >= len(candidates):
            return

        for i in range(candidate_map[candidates[next_index]] + 1):
            if target - candidates[next_index] * i >= 0:
                self.cal(candidates, target - candidates[next_index] * i, result,
                         current_list + [candidates[next_index]] * i,
                         next_index + 1, candidate_map)

