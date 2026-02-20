from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for i, v in enumerate(order):
            order_map[v] = i
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if not self.isSorted(words[i], words[j], order_map):
                    return False
        return True
    
    def isSorted(self, word1, word2, order_map):
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            a1 = order_map[word1[i]]
            b1 = order_map[word2[j]]
            if b1 < a1:
                return False
            elif b1 == a1:
                i += 1
                j += 1
            else:
                return True
        return i >= len(word1)

if __name__ == "__main__":
    sol = Solution()
    print(sol.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))  # True
    print(sol.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))  # False
    print(sol.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))  # False
