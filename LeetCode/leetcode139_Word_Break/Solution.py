from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        LeetCode 139. Word Break

        문자열 s와 단어 사전 wordDict가 주어질 때,
        s를 공백으로 구분된 사전 내 단어들의 연속으로 분할할 수 있는지 판별

        시간복잡도: O(n^2 * m) - n: 문자열 길이, m: 단어 평균 길이
        공간복잡도: O(n) - DP 배열
        """
        pass


# 테스트 케이스
if __name__ == "__main__":
    solution = Solution()

    # 테스트 1: s = "leetcode", wordDict = ["leet","code"]
    print("테스트 1:")
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    result1 = solution.wordBreak(s1, wordDict1)
    print(f's = "{s1}"')
    print(f"wordDict = {wordDict1}")
    print(f"결과: {result1}")
    print(f'예상: True ("leet" + "code")\n')

    # 테스트 2: s = "applepenapple", wordDict = ["apple","pen"]
    print("테스트 2:")
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    result2 = solution.wordBreak(s2, wordDict2)
    print(f's = "{s2}"')
    print(f"wordDict = {wordDict2}")
    print(f"결과: {result2}")
    print(f'예상: True ("apple" + "pen" + "apple")\n')

    # 테스트 3: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    print("테스트 3:")
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    result3 = solution.wordBreak(s3, wordDict3)
    print(f's = "{s3}"')
    print(f"wordDict = {wordDict3}")
    print(f"결과: {result3}")
    print(f'예상: False (분할 불가능)\n')

    # 테스트 4: s = "aaaaaaa", wordDict = ["aaaa","aaa"]
    print("테스트 4:")
    s4 = "aaaaaaa"
    wordDict4 = ["aaaa", "aaa"]
    result4 = solution.wordBreak(s4, wordDict4)
    print(f's = "{s4}"')
    print(f"wordDict = {wordDict4}")
    print(f"결과: {result4}")
    print(f'예상: True ("aaaa" + "aaa" or "aaa" + "aaaa")\n')

    # 테스트 5: s = "a", wordDict = ["a"]
    print("테스트 5:")
    s5 = "a"
    wordDict5 = ["a"]
    result5 = solution.wordBreak(s5, wordDict5)
    print(f's = "{s5}"')
    print(f"wordDict = {wordDict5}")
    print(f"결과: {result5}")
    print(f'예상: True\n')
