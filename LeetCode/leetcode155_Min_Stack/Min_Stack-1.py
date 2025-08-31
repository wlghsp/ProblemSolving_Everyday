class MinStack:
    def __init__(self):
        self.stack = [] # 하나의 스택으로 데이터와 최솟값 백을 모두 저장
        self.min = float('inf') # 현재 최솟값 추적

    def push(self, val: int) -> None:
        # 핵심: 새로운 최솟값이 나올 때마다 이전 최솟값을 백업
        if val <= self.min: # <= 사용하는 이유: 중복 최솟값도 처리해야 함
            self.stack.append(self.min) # 현재 최솟값을 백업 (복원용)
            self.min = val # 새로운 최솟값으로 백업

        self.stack.append(val) # 실제 데이터는 항상 추가

    def pop(self) -> None:
        popped = self.stack.pop() # 스택 최상단 제거

        # 최솟값을 제거하는 경우: 백업된 이전 최솟값 복원 필요
        if popped == self.min:
            self.min = self.stack.pop() # 바로 아래에 백업된 이전 최솟값 복원

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# 테스트 코드
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # -3이 나와야 함
    minStack.pop()
    print(minStack.top())     # 0이 나와야 함
    print(minStack.getMin())  # -2가 나와야 함