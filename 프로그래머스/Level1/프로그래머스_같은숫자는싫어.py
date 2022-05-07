# def solution(arr):
#     answer = []
#     for i in range(len(arr)):
#         if i == 0:
#             answer.append(arr[i])
#         elif arr[i] != arr[i - 1]:
#             answer.append(arr[i])

#     return answer


def solution(arr):
    a = []
    for i in arr:
        if a[-1:] == [i]:
            continue
        a.append(i)

    return a


arr = [1, 1, 3, 3, 0, 1, 1]
arr1 = [4, 4, 4, 3, 3]
print(solution(arr))
