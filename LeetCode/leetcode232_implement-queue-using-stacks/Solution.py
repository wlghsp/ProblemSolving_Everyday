class MyQueue:

    def __init__(self):
        self.stk = []
        self.sub_stk = []
        
    def push(self, x: int) -> None:
        self.stk.append(x)

    def pop(self) -> int:
        if not self.sub_stk:
            while self.stk:
                self.sub_stk.append(self.stk.pop())
        return self.sub_stk.pop()

    def peek(self) -> int:
        if not self.sub_stk:
            while self.stk:
                self.sub_stk.append(self.stk.pop())
        return self.sub_stk[-1]

    def empty(self) -> bool:
        return (len(self.stk) + len(self.sub_stk))== 0

if __name__ == "__main__":
    # Test case 1: 기본 동작
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())   # 1
    print(q.pop())    # 1
    print(q.empty())  # False

    # Test case 2: 단일 원소
    q2 = MyQueue()
    q2.push(5)
    print(q2.peek())  # 5
    print(q2.pop())   # 5
    print(q2.empty()) # True

    # Test case 3: 여러 push 후 순서 확인
    q3 = MyQueue()
    q3.push(1)
    q3.push(2)
    q3.push(3)
    print(q3.pop())   # 1
    print(q3.pop())   # 2
    q3.push(4)
    print(q3.pop())   # 3
    print(q3.pop())   # 4
