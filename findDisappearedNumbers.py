# # Given function
# class Solution(object):
#     def findDisappearedNumbers(self, nums):
#         s = set(nums)
#         disappeared = []
#         for i in range(1, len(nums) + 1):
#             if i not in s:
#                 disappeared.append(i)
#         return disappeared


class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])

        result = [i + 1 for i, num in enumerate(nums) if num > 0]
        return result


# Test cases
solution = Solution()

# Example 1
nums_1 = [4, 3, 2, 7, 8, 2, 3, 1]
output_1 = solution.findDisappearedNumbers(nums_1)
print("Example 1:")
print("Input:", nums_1)
print("Output:", output_1)

# Example 2
nums_2 = [1, 1]
output_2 = solution.findDisappearedNumbers(nums_2)
print("\nExample 2:")
print("Input:", nums_2)
print("Output:", output_2)
