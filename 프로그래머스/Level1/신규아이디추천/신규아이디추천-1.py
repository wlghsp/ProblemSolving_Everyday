def solution(new_id):
    #1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    first = new_id.lower()

    #2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    second = get_second(first)

    #3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    third = get_third(second)

    #4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if third and third[0] == '.':
        third = third[1:]
    if third and third[-1] == '.':
        third = third[:-1]

    #5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if not third:
        third = 'a'

    #6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(third) >= 16:
        third = third[:15]
        if third[-1] == '.':
            third = third[:-1]

    #7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(third) <= 2:
        while len(third) < 3:
            third += third[-1]
    return third

def get_second(temp):
    second = ''
    for c in temp:
        if (c.isalpha() and c.islower()) or c.isdigit() or c in ['-', '_', '.']:
            second += c
    return second

def get_third(second):
    third = ''
    i = 0
    while i < len(second):
        if second[i] == '.':
            third += '.'
            while i < len(second) and second[i] == '.':
                i += 1
        else:
            third += second[i]
            i += 1
    return third


print(solution("...!@BaT#*..y.abcdefghijklm")) # "bat.y.abcdefghi"
# print(solution("z-+.^.")) # "z--"
# print(solution("=.=")) # "aaa"
