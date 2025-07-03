class Solution:
    def kthCharacter(self, k: int) -> str:
        def generate(w):
            return [chr(ord(c) + 1) for c in w]

        word = ["a"] # 문자열보다는 리스트로 성능 개선
        while len(word) < k:
            word += generate(word)

        return word[k - 1]

if __name__ == "__main__":
    s = Solution()
    print(s.kthCharacter(5)) # b