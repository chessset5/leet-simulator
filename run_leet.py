"""
single runner for leet, use for debugging
"""

# pylint: disable=W0611

import json
from typing import Any

from leet import Solution
from LeetTypes.single_list_node import ListNode, list_to_node, node_to_list

# add input below

s = Solution()


# ret: Any = s.findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"])
# ret: Any = s.findSubstring(s="barfoothefoobarman", words=["foo", "bar"])

bs: dict = {}
with open("./test_repeating_characters_extended_extended.json", "r", encoding="utf-8") as file:
    bs = dict(json.load(file))
ret: Any = s.findSubstring(s=bs["s"], words=bs["words"])


print(ret)
