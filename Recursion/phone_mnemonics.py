'''
Leetcode 

Approach:
    recursion and backtracking
'''
class Solution:
    def letterCombinations(self, digits: str):
        if len(digits)==0:
            return []
        
        mapp = ["", "", "abc", "def","ghi","jkl", "mno", "pqrs", "tuv","wxyz"]
        result = []
        
        def recurse(curr, partial):
            if len(partial)==len(digits):
                char = "".join(partial)
                result.append(char)
                return
            
            curr_letter = mapp[int(digits[curr])]
            for char in curr_letter:
                partial.append(char)
                recurse(curr+1,partial)
                partial.pop()
                
        recurse(0, [])
        return result
sol = Solution()
print(sol.letterCombinations("2379"))