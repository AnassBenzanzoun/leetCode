class Solution(object):
    # def romanToInt(self, s):
    #     roman_to_integer = {
    #         "I": 1,
    #         "V": 5,
    #         "X": 10,
    #         "L": 50,
    #         "C": 100,
    #         "D": 500,
    #         "M": 1000,
    #     }
    #     result = 0
    #     i = 0
    #     reversed(s)
    #     while i < len(s):
    #         try:
    #             if s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X"):
    #                 result += roman_to_integer[s[i + 1]] - roman_to_integer[s[i]]
    #                 i += 2
    #             elif s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C"):
    #                 result += roman_to_integer[s[i + 1]] - roman_to_integer[s[i]]
    #                 i += 2
    #             elif s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"):
    #                 result += roman_to_integer[s[i + 1]] - roman_to_integer[s[i]]
    #                 i += 2
    #             else:
    #                 result += roman_to_integer[s[i]]
    #                 i += 1
    #         except IndexError:
    #             result += roman_to_integer[s[i]]
    #             i += 1
    #     return result
    def romanToInt(self, s):
        roman_to_integer = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        prev_value = 0
        for ch in reversed(s):
            current_value = roman_to_integer[ch]
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value
            prev_value = current_value
        return result


# Example 1
solution = Solution()
result1 = solution.romanToInt("III")
print(result1)  # Output: 3

# Example 2
result2 = solution.romanToInt("LVIII")
print(result2)  # Output: 58

# Example 3
result3 = solution.romanToInt("MCMXCIV")
print(result3)  # Output: 1994
