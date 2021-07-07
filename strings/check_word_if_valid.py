"""
1003. Check If Word Is Valid After Substitutions

example1:
Input: "aabcbc"
Output: true
Explanation:
We start with the valid string "abc".
Then we can insert another "abc" between "a" and "bc",
resulting in "a" + "abc" + "bc" which is "aabcbc".

example2:
Input: "abccba"
Output: false


"""


class Solution:

    # checks the validity of the string
    def isValid(self, S: str) -> bool:
        lis = []
        k = 0
        for i in range(len(S)):
            if S[i] == 'c' and k > 1 and lis[k - 1] == 'b' and lis[k - 2] == 'a':
                k -= 2
                lis.pop()
                lis.pop()
            else:
                lis.append(S[i])
                k += 1
        return k == 0

    # evaluate the provided test cases
    def testCases(self):
        words = ["aabcbc", "abcabcababcc", "abccba", "cababc"]
        valid = []
        invalid = []
        for word in words:
            if self.isValid(word):
                valid.append(word)
            else:
                invalid.append(word)
        return valid, invalid


if __name__ == "__main__":
    sol = Solution()
    valid, invalid = sol.testCases()
    print("Valid words are:    ", valid)
    print("Invalid words are:   ", invalid)


