class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for key, value in enumerate(nums):
            if key != value:
                return key
        return len(nums)


# Test Case 1
nums1 = [3, 0, 1]
print(Solution().missingNumber(nums1))  # Expected Output: 2

# Test Case 2
nums2 = [0, 1]
print(Solution().missingNumber(nums2))  # Expected Output: 2

# Test Case 3
nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(Solution().missingNumber(nums3))  # Expected Output: 8
