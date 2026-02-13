class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        for c in s:
            hm[c] = hm.get(c, 0) + 1
        for c in t:
            hm[c] = hm.get(c, 0) - 1
        return all(v == 0 for v in hm.values())


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    print(f"Test 1: {sol.isAnagram('anagram', 'nagaram')}")  # Expected: True

    # Test case 2
    print(f"Test 2: {sol.isAnagram('rat', 'car')}")  # Expected: False

    # Test case 3
    print(f"Test 3: {sol.isAnagram('listen', 'silent')}")  # Expected: True

    # Test case 4
    print(f"Test 4: {sol.isAnagram('a', 'ab')}")  # Expected: False

    # Test case 5
    print(f"Test 5: {sol.isAnagram('', '')}")  # Expected: True
