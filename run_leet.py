"""
single runner for leet, use for debugging
"""

# pylint: disable=W0611

from typing import Any

from leet import Solution
from LeetTypes.single_list_node import ListNode, list_to_node, node_to_list

# add input below

s = Solution()


# ret: Any = s.findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"])
ret: Any = s.findSubstring(s="barfoothefoobarman", words=["foo", "bar"])

print(ret)
