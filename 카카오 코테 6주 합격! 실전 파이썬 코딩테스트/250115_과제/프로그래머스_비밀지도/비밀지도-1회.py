def to_binary(number, n):
    result = ""
    while number != 0:
        result += str(number % 2)
        number //= 2
    return ''.join(reversed(result)).zfill(n)

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        row = (bin(arr1[i] | arr2[i])[2:].zfill(n)
               .replace('1', '#')
               .replace('0', ' '))

        answer.append(row)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
