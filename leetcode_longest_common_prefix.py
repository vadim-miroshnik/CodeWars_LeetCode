# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
class Solution:
    def longestCommonPrefix1(self, strs: list[str]) -> str:
        res = list(strs[0])
        for word in strs[1:]:
            for i, _ in enumerate(res):
                if len(word) == i or res[i] != word[i]:
                    res = res[:i]
                    if not res:
                        return ""
                    else:
                        break
        return "".join(res)

    def longestCommonPrefix2(self, strs: list[str]) -> str:
        if not len(strs):
            return ''
        i = 0
        for i, chars in enumerate(zip(*strs), 1):  # The resulting iterator stops when the shortest input is exhausted.
            if len(set(chars)) != 1:
                i -= 1
                break
        return strs[0][:i]


sol = Solution()
res = sol.longestCommonPrefix2(["flower", "flow", "flight"])
print(res)
res = sol.longestCommonPrefix2(["dog", "racecar", "car"])
print(res)
res = sol.longestCommonPrefix2([""])
print(res)
res = sol.longestCommonPrefix2(["ab", "a"])
print(res)
res = sol.longestCommonPrefix2(["leets", "leetsode", "leet"])
print(res)