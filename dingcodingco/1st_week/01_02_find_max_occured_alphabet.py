def find_alphabet_occurence_array(string):
    alphabet = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        alphabet[ord(char) - ord('a')] += 1
    return alphabet


def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    alphabet = find_alphabet_occurence_array(string)

    max_alphabet_index = 0
    max_occurrence = 0
    for i in range(len(alphabet)):
        if alphabet[i] > max_occurrence:
            max_occurrence = alphabet[i]
            max_alphabet_index = i


    return chr(ord('a') + max_alphabet_index)


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))