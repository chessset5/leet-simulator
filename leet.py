"""
Problem

`30. Substring with Concatenation of All Words`

<https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/>

You are given a string s and an array of strings words.
All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any
permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef",
"cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not
a concatenated string because it is not the concatenation of any permutation of
words.
Return an array of the starting indices of all the concatenated substrings in s.
You can return the answer in any order.

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of
["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of
["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of
["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of
["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of
["the","foo","bar"].

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.


"""

# pylint: disable=W0611

from typing import List, Optional

from LeetTypes.single_list_node import ListNode, node_to_list, repr_node
from MyTypes.debug_rep.vis_index import BinIntIndex, StrIndex

# pylint: disable=C0115
# pylint: disable=C0116
# pylint: disable=C0200


class Solution:
    master: set[str] = set()

    def subList(self, words: list[str], i: int) -> list[str]:
        return words[:i] + words[i + 1 :]

    def canConcat(self, s: str, words: list[str], start: str) -> bool:
        # checking master cache
        for m in self.master:
            if s.startswith(m):
                return True

        start_string: str = s
        go_next: bool = True
        while go_next:
            i: int = 0
            go_next = False
            while len(s) and i < len(words):
                w: str = words[i]
                if s.startswith(w):
                    s = s[len(w) :]
                    words = self.subList(words, i)
                    i -= 1
                    go_next = True
                i += 1
            if len(words) == 0:
                concat: str = start_string.replace(s, "")
                self.master.add(start + concat)
        return len(words) == 0

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        indexes: list[int] = []
        min_chars: int = len("".join(words))
        checked_words: set[str] = set()
        for i in range(len(words)):
            w: str = words[i]  # word
            if w in checked_words:
                continue
            checked_words.add(w)
            go: bool = True  # iterator condition
            p: int = 0  # possition
            first: bool = True  # variable for checking if concat is possible
            while go:
                go = False
                p = s.find(w, p)  # look for the next possition
                if first and p == -1:
                    # word doesn't exist, concat not possible
                    return []
                if p > -1:
                    go = True
                    first = False
                    substr: str = s[p + len(w) :]
                    if (p + min_chars) > len(s):
                        # no more pos to check
                        break
                    if self.canConcat(substr, self.subList(words, i), w):
                        indexes.append(p)
                    p += 1

        indexes.sort()
        return indexes
