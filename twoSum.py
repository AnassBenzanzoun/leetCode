def two_sum(nums, target):
    previous_values = {}
    for i in range(len(nums)):
        if (target - nums[i]) in previous_values:
            return [previous_values[target - nums[i]], i]
        previous_values[nums[i]] = i
    return []


# Example 1
nums1 = [2, 7, 11, 15]
target1 = 9
print(two_sum(nums1, target1))  # Output: [0, 1]

# Example 2
nums2 = [3, 2, 4]
target2 = 6
print(two_sum(nums2, target2))  # Output: [1, 2]

# Example 3
nums3 = [3, 3]
target3 = 6
print(two_sum(nums3, target3))  # Output: [0, 1]
