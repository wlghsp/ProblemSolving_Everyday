def birthdayCakeCandles(candles):
    # Write your code here
    maxValue = max(candles)
    # 리스트에서 중복 값 갯수 확인
    howMany = candles.count(maxValue)

    return howMany


candles_count = int(input().strip())

candles = list(map(int, input().rstrip().split()))

result = birthdayCakeCandles(candles)


print(result)
