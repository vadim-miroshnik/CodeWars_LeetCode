# 1160. Find Words That Can Be Formed by Characters
# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once).
# Return the sum of lengths of all good strings in words.
# Example 1:
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
class Solution:
    def countCharacters1(self, words: list[str], chars: str) -> int:
        """ my first attempt"""
        res = 0
        for word in words:
            chars_list = list(chars)
            chars_found = 0
            for char in word:
                if char in chars_list:
                    chars_list.remove(char)
                    chars_found += 1
            if chars_found == len(word):
                res += len(word)
        return res

    def countCharacters2(self, words: list[str], chars: str) -> int:
        """"best version from leetcode solutions """
        res = 0
        for word in words:
            for ch in word:
                if word.count(ch) > chars.count(ch):
                    break
            else:
                res += len(word)
        return res


sol = Solution()
res = sol.countCharacters2(["cat", "bt", "hat", "tree"], "atach")
print(res)

res = sol.countCharacters2(["hello", "world", "leetcode"], "welldonehoneyr")
print(res)
