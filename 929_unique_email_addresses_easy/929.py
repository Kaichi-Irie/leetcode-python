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
        S = set()
        for email in emails:
            atmark_pos = -1
            plus_pos = len(email)
            for pos, c in enumerate(email):
                if c == PLUS:
                    plus_pos = min(plus_pos, pos)
                elif c == ATMARK:
                    atmark_pos = pos
                    break
            if atmark_pos == -1 or atmark_pos == 0:
                return -1

            local_name = email[: min(atmark_pos, plus_pos)].replace(".", "")
            domain_name = email[atmark_pos:]
            forwarded_email = local_name + domain_name
            S.add(forwarded_email)
        return len(S)


# @lc code=end
