# Given a string s, return the length of the longest 
# substring
#  that contains at most two distinct characters.

# Example 1:

# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which its length is 3.
# Example 2:

# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        l = 0
        r = n
        ans = 0
        res = 0
        dic = {}
        for i in range(n):
            if s[i] not in dic:
                dic[s[i]] = 0
            dic[s[i]] += 1
            res += 1
            while len(dic) > 2:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l += 1
                res -= 1
            ans = max(ans,res)
        return ans