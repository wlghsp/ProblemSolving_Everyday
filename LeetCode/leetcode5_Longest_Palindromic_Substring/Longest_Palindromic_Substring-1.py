class Solution:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        # DP 테이블 초기화
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1

        # 한 글자는 항상 회문
        for i in range(n):
            dp[i][i] = True


        # 두 글자 확인
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2
                
        # 길이 3 이상
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # 양 끝이 같고 내부가 회문이면
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_len = length
        return s[start: start + max_len]


    def longestPalindrome_expand_around_center(self, s: str) -> str:
        def expand_around_center(left: int, right: int):
            # 중심에서 확장하며 회문 길이 반환
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1 # 실제 회문 길이
        
        if not s:
            return ""
        
        start = 0
        max_len = 0

        for i in range(len(s)):
            # 홀수 길이 회문 (중심이 한 문자)
            len1 = expand_around_center(i, i)
            # 짝수 길이 회문 (중심이 두 문자 사이)
            len2 = expand_around_center(i, i + 1)

            # 더 긴 것 선택
            current_len = max(len1, len2)

            # 최대 길이 갱신
            if current_len > max_len:
                max_len = current_len
                # 시작 위치 계산
                start = i - (current_len - 1) // 2
        return s[start:start + max_len]

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad")) # "bab"