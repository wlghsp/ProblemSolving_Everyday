
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)

        if len_s > len(t):
            return False # s가 t보다 길이가 길면 subSequence가 될 수 없다
        if len_s == 0:
            return True # s가 공백이라면 True 반환


        cnt = 0

        for val in t:
            if val == s[cnt]: # s의 0부터 확인해서, 알파벳이 있으면 cnt를 증가시킴.
                cnt += 1

                if cnt == len_s: # cnt가 증가해서 s의 길이와 같아지면 subsequence로 True를 반환
                    return True

        return False # 탐색했지만 cnt가 s의 알파벳을 다 찾지 못하였으므로 False를 반환



sol = Solution()

print(sol.isSubsequence("abc", "ahbgdc"))