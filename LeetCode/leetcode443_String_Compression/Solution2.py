from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        write, read = 0, 0
        n = len(chars)

        while read < n:
            current_char = chars[read]
            count = 0

            while read < n and current_char == chars[read]:
                count += 1
                read += 1

            chars[write] = current_char
            write += 1

            if count > 1:

                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write



# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    chars1 = ["a", "a", "b", "b", "c", "c", "c"]
    result1 = solution.compress(chars1)
    print(f"Test 1: {result1}, chars: {chars1[:result1]}")
    # Expected: 6, chars: ["a", "2", "b", "2", "c", "3"]

    # Test case 2
    chars2 = ["a"]
    result2 = solution.compress(chars2)
    print(f"Test 2: {result2}, chars: {chars2[:result2]}")
    # Expected: 1, chars: ["a"]

    # Test case 3
    chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    result3 = solution.compress(chars3)
    print(f"Test 3: {result3}, chars: {chars3[:result3]}")
    # Expected: 4, chars: ["a", "b", "1", "2"]

    # Test case 4
    chars4 = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
    result4 = solution.compress(chars4)
    print(f"Test 4: {result4}, chars: {chars4[:result4]}")
    # Expected: 3, chars: ["a", "1", "0"]
