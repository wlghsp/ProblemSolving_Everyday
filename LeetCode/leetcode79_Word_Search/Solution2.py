from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass
    
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Word exists
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    print(sol.exist(board1, "ABCCED"))  # Expected: True

    # Test 2: Word exists (different path)
    board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    print(sol.exist(board2, "SEE"))  # Expected: True

    # Test 3: Word does not exist
    board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    print(sol.exist(board3, "ABCB"))  # Expected: False

    # Test 4: Single cell match
    board4 = [["A"]]
    print(sol.exist(board4, "A"))  # Expected: True

    # Test 5: Single cell no match
    board5 = [["A"]]
    print(sol.exist(board5, "B"))  # Expected: False