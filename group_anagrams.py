"""
49. Given an array of strings, group anagrams together.

Example1:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # implement prime number soln
        new = list(strs)  # 0(N), 0(N)
        lis = {}

        # 0(N*QlgQ)
        for i in range(len(new)):  # 0(N)
            new[i] = "".join(sorted(new[i]))  # QlgQ

        for i in range(len(new)):  # 0(N)
            if new[i] in lis:
                lis[new[i]].append(strs[i])
            else:
                lis[new[i]] = [strs[i]]

        toreturn = []

        for key in lis:  # 0(N)
            toreturn.append(lis[key])
        return toreturn

