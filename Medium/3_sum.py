def test(nums):
    nums.sort()
    ans = set()
    for curr in range(len(nums)):
        if curr > 0 and nums[curr] == nums[curr - 1]:
            continue
        low = curr + 1
        high = len(nums) - 1
        while low < high:
            temp_sum = nums[curr] + nums[low] + nums[high]
            if temp_sum == 0:
                ans.add((nums[curr], nums[low], nums[high]))
                low += 1
                high -= 1
            elif temp_sum > 0:
                high -= 1
            elif temp_sum < 0:
                low += 1

    return [list(small_list) for small_list in ans]


print (test([-1, 0, -1, 1, 2, 4]))
