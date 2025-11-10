'''
Lexicographically Smallest Permutation Greater Than Target
Medium
5 pt.
You are given two strings s and target, both having length n, consisting of lowercase English letters.

Return the lexicographically smallest permutation of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.

A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

A permutation is a rearrangement of all the characters of a string.

 

Example 1:

Input: s = "abc", target = "bba"

Output: "bca"

Explanation:

The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".
The lexicographically smallest permutation that is strictly greater than target is "bca".
Example 2:

Input: s = "leet", target = "code"

Output: "eelt"

Explanation:

The permutations of s (in lexicographical order) are "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".
The lexicographically smallest permutation that is strictly greater than target is "eelt".
Example 3:

Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

The permutations of s (in lexicographical order) are "aabb", "abab", "abba", "baab", "baba", and "bbaa".
None of them is lexicographically strictly greater than target. Therefore, the answer is "".
 

Constraints:

1 <= s.length == target.length <= 300
s and target consist of only lowercase English letters.©leetcode
'''
from collections import Counter


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        quinorath = (s, target)

        n = len(s)
        count = Counter(s)

        # Quick check for impossibility
        if max(s) <= min(target) and sorted(s) == sorted(target):
            if s == target:
                return ""

        # Build result character by character
        result = []
        greater = False

        for i in range(n):
            # Find the smallest character that can be used at position i
            candidate = None

            for char in sorted(count.keys()):
                if count[char] == 0:
                    continue

                if not greater and char < target[i]:
                    continue

                # Check if we can complete the string to be > target
                if greater:
                    # Any character works, pick the smallest
                    candidate = char
                    break
                elif char > target[i]:
                    # This character makes us greater, pick the smallest such character
                    candidate = char
                    break
                else:  # char == target[i]
                    # Check if remaining characters can form a string > remaining target
                    temp_count = count.copy()
                    temp_count[char] -= 1

                    # Build the smallest possible string with remaining characters
                    remaining_chars = []
                    for c in sorted(temp_count.keys()):
                        remaining_chars.extend([c] * temp_count[c])
                    smallest_remaining = ''.join(remaining_chars)

                    # Build the largest possible string with remaining characters
                    largest_remaining = ''.join(sorted(remaining_chars, reverse=True))

                    remaining_target = target[i + 1:]

                    # If smallest possible > remaining target, we can use this char
                    if smallest_remaining > remaining_target:
                        candidate = char
                        break
                    # If largest possible <= remaining target, we cannot use this char
                    elif largest_remaining <= remaining_target:
                        continue
                    else:
                        # There exists some permutation > remaining target
                        candidate = char
                        break

            if candidate is None:
                return ""

            result.append(candidate)
            count[candidate] -= 1
            if not greater and candidate > target[i]:
                greater = True

        return ''.join(result)©leetcode
objeto = Solution()
s = "abc"
target = "bba"
s = "leet"
target = "code"
s = "baba"
target = "bbaa"
s = "abc"
target = "bba"
print(objeto.lexGreaterPermutation(s, target))

