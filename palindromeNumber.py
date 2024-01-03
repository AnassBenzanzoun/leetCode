class Solution(object):
    def isPalindrome(self, x):
        return "".join(reversed(str(x))) == str(x)


solution = Solution()

# Example 1
x1 = 121
output1 = solution.isPalindrome(x1)
print(output1)  # Expected output: True

# Example 2
x2 = -121
output2 = solution.isPalindrome(x2)
print(output2)  # Expected output: False

# Example 3
x3 = 10
output3 = solution.isPalindrome(x3)
print(output3)  # Expected output: False
