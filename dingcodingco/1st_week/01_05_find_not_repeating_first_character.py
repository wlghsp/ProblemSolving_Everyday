input = "abadabac"

def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    for char in string:
        if char_count[char] == 1:
            return char

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))