class Solution:
    def kthCharacter(self, k: int) -> str:
        def generate(w):
            result = ""
            for c in w:
                result += chr(ord(c) + 1)
            return result

        word = "a"
        while len(word) < k:
            word += generate(word)
        print(word)
        return word[k - 1]

if __name__ == "__main__":
    s = Solution()
    print(s.kthCharacter(5)) # b