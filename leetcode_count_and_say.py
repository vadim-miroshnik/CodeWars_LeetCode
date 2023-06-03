# 38. Count and Say
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted 
# into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings such that each 
# substring contains exactly one unique digit. Then for each substring, say the number of digits, then say 
# the digit. Finally, concatenate every said digit.
# Given a positive integer n, return the nth term of the count-and-say sequence.
# Example 1:
# Input: n = 1
# Output: "1"
# Explanation: This is the base case.
# Example 2:
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
# https://leetcode.com/problems/count-and-say/
class Solution:
    def countAndSay(self, n: int) -> str:
        """recursive version"""
        def say(n: int) -> str:
            curr, cnt, res = 0, 0, ""
            for i in str(n):
                if curr == i:
                    cnt += 1
                else:
                    if cnt > 0:
                        res += str(cnt) + str(curr)
                    curr = i
                    cnt = 1
            res += str(cnt) + str(curr)
            return res

        if n == 1:
            return '1'
        else:
            prev = self.countAndSay(n-1)
            return say(prev)


sol = Solution()
res = sol.countAndSay(4)
print(res)

res = sol.countAndSay(1)
print(res)
