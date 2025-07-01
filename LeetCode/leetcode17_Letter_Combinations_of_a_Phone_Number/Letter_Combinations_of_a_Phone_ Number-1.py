from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_letter = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
        }

        answer = []
        def backtrack(picked, start):
            if len(picked) == len(digits):
                answer.append(picked)
                return

            alphabets = digit_to_letter[digits[start]]
            for c in alphabets:
                backtrack(picked + c, start + 1)

        backtrack("", 0)
        return answer


if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
