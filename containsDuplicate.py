# The problem is asking to return true if any value appears at least twice in the array,
# and return false if every element is distinct. The first thought that comes
# to mind is to use a data structure that can track the elements that we have seen so far while
# iterating through the array. A set is a perfect fit for this purpose because it only stores unique elements.
class Solution(object):
    def containsDuplicate(self, nums):
        result = set()
        for num in nums:
            if num in result:
                return True
            else:
                result.add(num)
        return False


# Test cases
# Example 1:
# Input
print("Input: nums = [1,2,3,1]")
# Output
print("Output:", Solution().containsDuplicate([1, 2, 3, 1]))

# Example 2:
print("Example 2:")
print("Input: nums = [1,2,3,4]")
print("Output:", Solution().containsDuplicate([1, 2, 3, 4]))

# Example 3:
print("Example 3:")
print("Input: nums = [1,1,1,3,3,4,3,2,4,2]")
print("Output:", Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
