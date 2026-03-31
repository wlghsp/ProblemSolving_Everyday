class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    n = 4
    k = 2
    result = sol.combine(n, k)
    print(f"Test 1 (n=4, k=2): {result}")
    # Expected: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

    # Test case 2
    n = 1
    k = 1
    result = sol.combine(n, k)
    print(f"Test 2 (n=1, k=1): {result}")
    # Expected: [[1]]

    # Test case 3
    n = 5
    k = 3
    result = sol.combine(n, k)
    print(f"Test 3 (n=5, k=3): {result}")
    # Expected: 10개 조합
    print(f"  Length: {len(result)}")
