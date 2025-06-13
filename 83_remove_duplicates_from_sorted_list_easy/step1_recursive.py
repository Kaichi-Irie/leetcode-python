#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # seen: set
        # _deleteDuplicates(node,seen)
        # if node.val is in seen:
        #   return _deleteDuplicates(node.next,seen)
        # else:
        #   add val to seen
        #   return Node(val,_deleteDuplicates(node.next,seen))
        seen = set()

        def _deleteDuplicates(start: ListNode, seen: set) -> ListNode:
            if start is None:
                return None
            if start.val in seen:
                return _deleteDuplicates(start.next, seen)
            seen.add(start.val)
            start.next = _deleteDuplicates(start.next, seen)
            return start

        return _deleteDuplicates(head, seen)


# @lc code=end
