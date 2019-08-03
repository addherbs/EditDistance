def threeSumClosest (nums, target):
    nums.sort()
    ans = dict()
    for curr in range(len(nums)):
        if curr > 0 and nums[curr] == nums[curr - 1]:
            continue
        low = curr + 1
        high = len(nums) - 1
        while low < high:
            temp_sum = nums[curr] + nums[low] + nums[high]
            if temp_sum == target:
                return temp_sum
            elif temp_sum > target:
                high -= 1
            elif temp_sum < target:
                low += 1
            ans[temp_sum] = abs(target - temp_sum)

    return min(ans, key=ans.get)

print(threeSumClosest([-1, 2, 1, 4], 1))

print(threeSumClosest([-3,-2,-5,3,-4],-1))
