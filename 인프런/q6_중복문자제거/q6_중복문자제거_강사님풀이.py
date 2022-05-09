



# ksekkset
str = input()
str_list = list(str)

list = []
for i in range(len(str)):
    # find는 처음부터 찾음. rfind는 뒤에서부터 찾음
    # 문자의 인덱스(위치)와 find로 나온 위치가 같다면 처음 나온 문자
    if str.find(str[i]) == i:
        list.append(str[i])

print(''.join(list))




