#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#
from typing import List


# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        PLUS = "+"
        ATMARK = "@"
        DOT = "."
        S = set()

        for email in emails:
            verbose_local, domain = email.split(ATMARK)
            local = verbose_local.split(PLUS)[0].replace(DOT, "")
            S.add(local + "@" + domain)
        return len(S)


# @lc code=end
