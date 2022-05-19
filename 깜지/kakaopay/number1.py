def solution(region, num, info):
    def calc(b, c, d):
        return (b + 1) * 2 + (c + 2) + (d + 1) * 5

    myList = list()
    for i, v in enumerate(info):
        score = calc(v[1], v[2], v[3])
        if v[0] == region:
            v[0] = 0
        else:
            v[0] = 1
        myList.append((v[0], score, i))

    myList.sort(key=lambda x: (x[0], -x[1], x[2]))
    answer = [-1] * len(myList)
    print(myList)

    if len(myList) >= num:
        for i in range(num):
            m = myList.pop(0)
            answer[m[2]] = i + 1
        return answer
    elif len(myList) < num:
        idx = 1
        for i in myList:
            answer[i[2]] = idx
            idx += 1
        return answer


region = 1
num = 7
info = [
    [1, 0, 2, 1],
    [2, 6, 5, 2],
    [3, 10, 2, 4],
    [1, 1, 5, 6],
    [2, 7, 10, 2],
    [3, 8, 6, 3],
]

print(solution(region, num, info))  # [-1, 2, 3, 4, 1, -1]
