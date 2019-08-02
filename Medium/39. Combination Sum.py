# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]


def cal(nums, target, result_test, current_list, next_index):
    # print(target, result_test, current_list, next_index)
    if target == 0:
        result_test.append(current_list)
        print("answer", current_list)
        return
    if target < 0 or next_index >= len(nums):
        return

    i = 0
    while (target - nums[next_index] * i >= 0):
        cal(nums, target - nums[next_index] * i, result_test, current_list + [nums[next_index]] * i, next_index + 1)
        i += 1


def call_cal():
    result = []
    # cal([2, 3, 6, 7], 7, result, [], 0)
    cal([2, 3, 5], 8, result, [], 0)
    print(result)

call_cal()
