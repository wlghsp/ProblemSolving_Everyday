N = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))
oper_dict = {i: op for i, op in zip(range(len(operator)), ["+", "-", "x", "/"])}

def operate(op, a, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "x":
        return a * b
    elif op == "/":
        return int(a / b)

min_val = float("inf")
max_val = float("-inf")
def recur(picked, op):
    global min_val, max_val
    if N - 1 == len(picked):
        # 계산 결과를 구한다
        num = nums[0]
        for i in range(N - 1):
            num = operate(picked[i], num, nums[i + 1])

        # 최대, 최소값 갱신
        min_val = min(min_val, num)
        max_val = max(max_val, num)

        return

    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            recur(picked + [oper_dict[i]], op)
            op[i] += 1

recur([], operator)
print(max_val, min_val, sep='\n')