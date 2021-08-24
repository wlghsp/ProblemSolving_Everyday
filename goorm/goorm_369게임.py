

n = int(input())

count = 0
for i in range(3, n):
    nums = list(str(i))
    for num in nums:
        if num == "3" or num == "6" or num == "9":
            count += 1

print(count)
