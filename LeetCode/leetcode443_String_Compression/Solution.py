from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        # write: 결과를 쓸 위치
        write = 0
        read = 0
        # read: 원본을 읽을 위치
        n = len(chars)

        while read < n:
            current_char = chars[read]
            count = 0

            # 같은 문자가 연속 몇 개인지 세기
            while read < n and chars[read] == current_char:
                read += 1
                count += 1
            
            # 문자 쓰기
            chars[write] = current_char
            write += 1

            # 개수가 2 이상이면 숫자도 쓰기
            if count > 1:
                # 숫자를 문자열로 변환 후 한 글자씩 쓰기
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
    print(f"Test 1: length={result1}, chars={chars1[:result1]}")
    # Expected: length=6, chars=['a', '2', 'b', '2', 'c', '3']

    # Test case 2
    chars2 = ["a"]
    result2 = solution.compress(chars2)
    print(f"Test 2: length={result2}, chars={chars2[:result2]}")
    # Expected: length=1, chars=['a']

    # Test case 3
    chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    result3 = solution.compress(chars3)
    print(f"Test 3: length={result3}, chars={chars3[:result3]}")
    # Expected: length=4, chars=['a', 'b', '1', '2']

    # Test case 4
    chars4 = ["a", "a", "a", "b", "b", "a", "a"]
    result4 = solution.compress(chars4)
    print(f"Test 4: length={result4}, chars={chars4[:result4]}")
    # Expected: length=6, chars=['a', '3', 'b', '2', 'a', '2']
