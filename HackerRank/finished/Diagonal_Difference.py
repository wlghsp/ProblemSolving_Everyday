def diagonalDifference(arr):
    # Write your code here
    length = len(arr)
    sum1 = 0
    sum2 = 0
    for i in range(length):
        sum1 += arr[i][i]
    for i in range(length):
        sum2 += arr[i][length-i-1]
    result = abs(sum1 - sum2)

    return result
